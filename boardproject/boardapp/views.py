from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy


@login_required
def signupfunc(request):
    if request.method == 'POST':

        """
        取得メソッド例
        """
        # all() でリスト取得
        all_user = User.objects.all()
        print(all_user)

        # get() は dic のメソッドと同じ　key指定で内容を取り出せる
        u_data = User.objects.get(username='user01')
        print(f"name : {u_data.username}  | mail : {u_data.email}")

        # POSTデータの内容を取得
        username = request.POST['user_name']
        password = request.POST['password']

        # ユーザが既に登録されているかどうかをチェック
        try:
            User.objects.get(username=username)
            return render(request, 'signup.html', {'error': '既に登録済みのユーザーです'})

        except:
            # ユーザ作成
            # https://docs.djangoproject.com/ja/2.2/topics/auth/default/#creating-users
            # 引数 : ユーザ名,　e-mail(任意), password
            user = User.objects.create_user(username, '', password)

            return render(request, 'signup.html', {'some': 9999})

    else:
        print('this is get method')

    return render(request, 'signup.html', {'some': 'some_data'})


def loginfunc(request):
    """
    ■ログインについてのdocument
    https://docs.djangoproject.com/ja/2.2/topics/auth/default/#how-to-log-a-user-in

    """
    if request.method == 'POST':
        # POSTデータの内容を取得
        username = request.POST['user_name']
        password = request.POST['password']

        # 認証
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirect to a success page.
            # render()でも可能
            return redirect('list')
        else:
            # Return an 'invalid login' error message.
            return redirect('login')
    else:
        # getメソッド（初回ルート）の場合
        return render(request, 'login.html')


"""
login_required デコレータ
https://docs.djangoproject.com/ja/2.2/topics/auth/default/#the-login-required-decorator

もしユーザがログインしていなければ、settings.LOGIN_URL にリダイレクトし、
クエリ文字列に現在の絶対パスを渡します。リダイレクト先の例: /accounts/login/?next=/polls/3/

"""


@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


"""
ユーザーをログアウトさせる
https://docs.djangoproject.com/ja/2.2/topics/auth/default/#how-to-log-a-user-out
"""


def logoutfunc(request):
    logout(request)
    return redirect('login')


def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object': object})


def goodfunc(request, pk):
    """
    いいねボタンの挙動
    :param request:
    :param pk:
    :return:
    """
    post = BoardModel.objects.get(pk=pk)
    post.good += 1

    # save することで、DBに書き込みが走る
    post.save()

    # 処理が終わったらリスト画面を表示
    return redirect('list')


def readfunc(request, pk):
    """
    既読ボタンの挙動
    :param request:
    :param pk:
    :return:
    """
    post = BoardModel.objects.get(pk=pk)

    # ログインしているユーザ情報を取得(フレームワークが入れてくれている)
    # session情報を使ってログインした時点でrequestオブジェクトにuser情報が格納される
    read_user_name = request.user.get_username()

    # 既に現在のユーザが既読ボタンを押していないかをチェック
    if read_user_name in post.readtext:
        # print(f"post.readtext = {post.readtext}")
        return redirect('list')
    else:
        post.read += 1

        # 説明をわかりやすくする為、人の名前を入れるような簡易実装になっている
        post.readtext = post.readtext + ' ' + read_user_name

        post.save()
        # print(f"post.readtext = {post.readtext}")
        return redirect('list')


class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')
