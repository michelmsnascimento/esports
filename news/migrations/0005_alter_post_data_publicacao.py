# Generated by Django 4.1.2 on 2022-10-30 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 10, 30, 20, 42, 30, 643550, tzinfo=datetime.timezone.utc)),
        ),
    ]
