# Generated by Django 3.0.4 on 2021-11-17 20:51

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='タイトル')),
                ('prefecture', models.CharField(max_length=4, verbose_name='都道府県')),
                ('content', models.CharField(max_length=1000, verbose_name='内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '釣行',
                'db_table': 'trip',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fish_name', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^([ァ-ン]|ー)+$', '全角カナで入力してください')], verbose_name='魚名')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='画像(任意)')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='投稿日時')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Trip')),
            ],
            options={
                'verbose_name': '釣果',
                'db_table': 'result',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, verbose_name='コメント内容')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='投稿日時')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'コメント',
                'db_table': 'comment',
            },
        ),
    ]
