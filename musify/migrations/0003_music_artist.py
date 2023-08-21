# Generated by Django 4.2.4 on 2023-08-15 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musify', '0002_songs_trending'),
    ]

    operations = [
        migrations.CreateModel(
            name='music_artist',
            fields=[
                ('songs_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='musify.songs')),
            ],
            bases=('musify.songs',),
        ),
    ]
