# Generated by Django 4.2.4 on 2024-07-31 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0005_alter_song_album_alter_song_audio_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
