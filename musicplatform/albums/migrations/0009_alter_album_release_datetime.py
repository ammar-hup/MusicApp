# Generated by Django 4.2.4 on 2023-11-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0008_alter_album_release_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_datetime',
            field=models.DateTimeField(default='2000/12/12'),
        ),
    ]
