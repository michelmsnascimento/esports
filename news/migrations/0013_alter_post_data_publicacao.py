# Generated by Django 4.1.2 on 2022-11-17 02:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 11, 17, 2, 40, 3, 472252, tzinfo=datetime.timezone.utc)),
        ),
    ]
