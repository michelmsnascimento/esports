# Generated by Django 4.1.2 on 2022-11-13 17:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneios', '0007_alter_torneios_data_partida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torneios',
            name='data_partida',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 11, 13, 17, 11, 30, 292533, tzinfo=datetime.timezone.utc)),
        ),
    ]
