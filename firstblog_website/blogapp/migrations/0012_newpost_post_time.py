# Generated by Django 4.0.1 on 2023-01-03 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0011_remove_newpost_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpost',
            name='post_time',
            field=models.DateField(default=datetime.date(2023, 1, 3), max_length=200, null=True),
        ),
    ]
