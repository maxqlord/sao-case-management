# Generated by Django 2.0.5 on 2018-05-31 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0019_auto_20180527_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='slug',
        ),
    ]
