# Generated by Django 4.1.2 on 2022-11-13 22:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneios', '0011_alter_torneios_data_partida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torneios',
            name='data_partida',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 11, 13, 22, 32, 57, 668213, tzinfo=datetime.timezone.utc)),
        ),
    ]
