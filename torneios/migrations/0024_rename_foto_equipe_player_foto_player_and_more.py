# Generated by Django 4.1.2 on 2022-11-17 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneios', '0023_rename_toneios_equipe_torneios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='foto_equipe',
            new_name='foto_player',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='nome_equipe',
            new_name='nome_player',
        ),
        migrations.AddField(
            model_name='player',
            name='torneios',
            field=models.ManyToManyField(to='torneios.torneios'),
        ),
    ]
