from django.shortcuts import render
from django.contrib.auth.models import User


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

        # ユーザ作成
        # https://docs.djangoproject.com/ja/2.2/topics/auth/default/
        # 引数 : ユーザ名,　e-mail(任意), password
        user = User.objects.create_user(username, '', password)

        return render(request, 'signup.html', {'some': 9999})

    else:
        print('this is get method')

    return render(request, 'signup.html', {'some': 'some_data'})
