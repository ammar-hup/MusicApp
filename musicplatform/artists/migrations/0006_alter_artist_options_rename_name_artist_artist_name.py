# Generated by Django 4.2.4 on 2023-11-18 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0005_remove_artist_sociallink_artist_social_link_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['artist_name'], 'verbose_name': 'Artist'},
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='name',
            new_name='artist_name',
        ),
    ]
