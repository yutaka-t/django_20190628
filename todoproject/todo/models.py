from django.db import models

"""モデルフィールドの参考
    ■Qiita : Django: モデルフィールドリファレンスの一覧
        https://qiita.com/nachashin/items/f768f0d437e0042dd4b3

    ■モデルフィールドリファレンス | Django ドキュメント | Django
        https://docs.djangoproject.com/ja/1.11/ref/models/fields/
"""

# 選択肢はタプル型で実装できる
# (<実際にHTMLに埋め込む文字列>, <画面で表示する文字列>)
PRIORITY = (('danger', '緊急'), ('info', '通常'), ('success', 'そのうち'))


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY,
    )
    duedate = models.DateField()

    def __str__(self):
        return self.title
