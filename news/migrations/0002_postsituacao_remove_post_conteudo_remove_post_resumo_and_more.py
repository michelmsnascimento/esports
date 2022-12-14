# Generated by Django 4.1.2 on 2022-11-28 02:16

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_alter_perfil_foto'),
        ('torneios', '0044_player_equipe_alter_equipe_foto_equipe_and_more'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostSituacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='conteudo',
        ),
        migrations.RemoveField(
            model_name='post',
            name='resumo',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subtitulo',
        ),
        migrations.AddField(
            model_name='post',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='torneios.game'),
        ),
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 11, 28, 2, 16, 40, 134260, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('posts', models.ManyToManyField(to='news.post')),
            ],
        ),
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('posts', models.ManyToManyField(through='news.PostSituacao', to='news.post')),
            ],
        ),
        migrations.AddField(
            model_name='postsituacao',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post'),
        ),
        migrations.AddField(
            model_name='postsituacao',
            name='situacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.situacao'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(max_length=1024)),
                ('perfil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contas.perfil')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post')),
            ],
        ),
        migrations.CreateModel(
            name='Assunto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('posts', models.ManyToManyField(to='news.post')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='postsituacao',
            unique_together={('post', 'situacao')},
        ),
    ]
