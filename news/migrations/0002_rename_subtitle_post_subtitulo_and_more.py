# Generated by Django 4.1.2 on 2022-10-25 03:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='subtitle',
            new_name='subtitulo',
        ),
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 25, 3, 20, 48, 127107, tzinfo=datetime.timezone.utc)),
        ),
    ]