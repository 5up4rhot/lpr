# Generated by Django 2.1.5 on 2019-01-30 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-createtime',)},
        ),
    ]
