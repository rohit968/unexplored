# Generated by Django 3.0.5 on 2020-08-31 07:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('unexplored', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 31, 7, 34, 51, 283193, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
