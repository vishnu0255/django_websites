# Generated by Django 4.0.1 on 2022-12-14 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_id',
            field=models.IntegerField(null=True),
        ),
    ]