# Generated by Django 5.0.6 on 2024-06-17 17:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_day', models.DateField(default=datetime.datetime(2000, 1, 1, 0, 0))),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
