# Generated by Django 4.1.2 on 2022-11-17 00:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneios', '0015_alter_torneios_data_partida'),
    ]

    operations = [
        migrations.RenameField(
            model_name='torneios',
            old_name='subtitulo',
            new_name='nome',
        ),
        migrations.AlterField(
            model_name='torneios',
            name='data_partida',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 11, 17, 0, 15, 11, 125672, tzinfo=datetime.timezone.utc)),
        ),
    ]
