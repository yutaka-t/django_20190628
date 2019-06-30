from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



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
            return redirect('signup')
        else:
            # Return an 'invalid login' error message.
            return redirect('signup')
    else:
        # getメソッド（初回ルート）の場合
        return render(request, 'login.html')
