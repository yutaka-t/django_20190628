# Generated by Django 2.2.2 on 2019-07-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='good',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='read',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='readtext',
            field=models.CharField(default='', max_length=200),
        ),
    ]
