# Generated by Django 4.1.2 on 2022-11-27 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torneios', '0032_remove_player_equipe_partida_equipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rodada',
            name='torneios',
        ),
        migrations.AddField(
            model_name='rodada',
            name='torneios',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='torneios.torneios'),
            preserve_default=False,
        ),
    ]
