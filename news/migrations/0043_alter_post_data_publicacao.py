# Generated by Django 4.1.2 on 2022-11-27 19:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0042_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 11, 27, 19, 1, 21, 594376, tzinfo=datetime.timezone.utc)),
        ),
    ]