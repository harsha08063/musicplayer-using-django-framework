# Generated by Django 4.2.4 on 2023-08-15 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='songs',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=1000)),
                ('singer', models.CharField(default='', max_length=1000)),
                ('image', models.ImageField(default='', upload_to='images')),
                ('songs', models.FileField(default='', upload_to='songs')),
                ('movie', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='likedsongs',
            fields=[
                ('liked_id', models.AutoField(primary_key=True, serialize=False)),
                ('music_id', models.CharField(default='', max_length=100000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
