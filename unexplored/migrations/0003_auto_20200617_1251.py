# Generated by Django 3.0.7 on 2020-06-17 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unexplored', '0002_auto_20200616_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
