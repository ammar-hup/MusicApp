# Generated by Django 4.2.4 on 2023-08-09 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_alter_artist_options_alter_artist_sociallink'),
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['name'], 'verbose_name': 'Album'},
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='artists.artist'),
            preserve_default=False,
        ),
    ]
