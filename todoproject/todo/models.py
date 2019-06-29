from django.db import models

"""モデルフィールドの参考
    ■Qiita : Django: モデルフィールドリファレンスの一覧
        https://qiita.com/nachashin/items/f768f0d437e0042dd4b3

    ■モデルフィールドリファレンス | Django ドキュメント | Django
        https://docs.djangoproject.com/ja/1.11/ref/models/fields/
"""


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()

    def __str__(self):
        return self.title
