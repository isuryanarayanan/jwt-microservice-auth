# Generated by Django 3.2 on 2021-04-25 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthSecret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret', models.TextField(default='')),
                ('secret_size', models.IntegerField(default=156)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='investorprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='AdministratorProfile',
        ),
        migrations.DeleteModel(
            name='InvestorProfile',
        ),
    ]
