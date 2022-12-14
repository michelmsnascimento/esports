# Generated by Django 4.1.2 on 2022-11-17 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneios', '0016_rename_subtitulo_torneios_nome_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='torneios',
            name='data_partida',
        ),
        migrations.RemoveField(
            model_name='torneios',
            name='resumo',
        ),
        migrations.AddField(
            model_name='equipe',
            name='torneios',
            field=models.ManyToManyField(to='torneios.torneios'),
        ),
        migrations.AddField(
            model_name='torneios',
            name='data_torneio',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Rodada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('data_partida', models.DateTimeField(blank=True, null=True)),
                ('torneios', models.ManyToManyField(to='torneios.torneios')),
            ],
        ),
    ]
