# Generated by Django 4.1.2 on 2022-11-26 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torneios', '0027_situacao_torneiosituacao_situacao_torneio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rodada', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='torneios.rodada')),
            ],
        ),
    ]
