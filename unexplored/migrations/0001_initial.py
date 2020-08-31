# Generated by Django 3.0.5 on 2020-08-31 04:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2020, 8, 31, 4, 55, 32, 456067, tzinfo=utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Article',
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField()),
                ('approved_comment', models.BooleanField(default=False)),
                ('article_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='unexplored.Article')),
            ],
            options={
                'verbose_name_plural': 'Comment',
                'ordering': ('-created_date',),
            },
        ),
    ]
