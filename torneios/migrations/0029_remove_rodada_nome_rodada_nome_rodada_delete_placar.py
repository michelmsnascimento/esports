# Generated by Django 4.1.2 on 2022-11-26 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneios', '0028_placar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rodada',
            name='nome',
        ),
        migrations.AddField(
            model_name='rodada',
            name='nome_rodada',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.DeleteModel(
            name='Placar',
        ),
    ]
