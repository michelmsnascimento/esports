# Generated by Django 4.1.2 on 2022-11-17 02:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 11, 17, 2, 38, 19, 253073, tzinfo=datetime.timezone.utc)),
        ),
    ]