# Generated by Django 4.1.2 on 2022-11-17 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('torneios', '0022_remove_equipe_toneios_equipe_toneios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipe',
            old_name='toneios',
            new_name='torneios',
        ),
    ]
