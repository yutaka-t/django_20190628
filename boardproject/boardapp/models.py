from django.db import models


class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)

    # upload_to への指定は、Settingsに指定した場所からさらに場所を絞る場合に利用する
    # 空欄だと、Settings の設定箇所となる
    images = models.ImageField(upload_to='')

    # いいね
    good = models.IntegerField(null=True, blank=True, default=0)

    # 既読(既読数)
    read = models.IntegerField(default=0)

    # 既読(既読ユーザの記録)
    readtext = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.title
