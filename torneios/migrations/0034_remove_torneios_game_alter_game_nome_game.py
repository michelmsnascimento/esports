# Generated by Django 4.1.2 on 2022-11-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneios', '0033_remove_rodada_torneios_rodada_torneios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='torneios',
            name='game',
        ),
        migrations.AlterField(
            model_name='game',
            name='nome_game',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
