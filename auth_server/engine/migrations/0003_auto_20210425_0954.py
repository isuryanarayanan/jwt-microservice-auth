# Generated by Django 3.2 on 2021-04-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0002_auto_20210425_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='secret',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='secret_size',
            field=models.IntegerField(default=156),
        ),
    ]
