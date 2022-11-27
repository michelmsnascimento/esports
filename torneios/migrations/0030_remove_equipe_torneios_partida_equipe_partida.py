# Generated by Django 4.1.2 on 2022-11-27 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneios', '0029_remove_rodada_nome_rodada_nome_rodada_delete_placar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='torneios',
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_partida', models.CharField(blank=True, max_length=150, null=True)),
                ('data_partida', models.DateTimeField(blank=True, null=True)),
                ('partida', models.ManyToManyField(to='torneios.rodada')),
            ],
        ),
        migrations.AddField(
            model_name='equipe',
            name='partida',
            field=models.ManyToManyField(to='torneios.partida'),
        ),
    ]
