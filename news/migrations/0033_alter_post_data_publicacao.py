# Generated by Django 4.1.2 on 2022-11-27 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0032_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 11, 27, 17, 27, 59, 497738, tzinfo=datetime.timezone.utc)),
        ),
    ]
