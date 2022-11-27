# Generated by Django 4.1.2 on 2022-11-14 02:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_alter_perfil_foto'),
        ('news', '0002_postsituacao_remove_post_conteudo_remove_post_resumo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contas.perfil'),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 11, 14, 2, 44, 0, 771398, tzinfo=datetime.timezone.utc)),
        ),
    ]
