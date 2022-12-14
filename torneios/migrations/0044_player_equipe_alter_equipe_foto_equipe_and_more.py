# Generated by Django 4.1.2 on 2022-11-27 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneios', '0043_player_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='equipe',
            field=models.ManyToManyField(to='torneios.equipe'),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='foto_equipe',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/equipe'),
        ),
        migrations.AlterField(
            model_name='player',
            name='foto_player',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/player'),
        ),
    ]
