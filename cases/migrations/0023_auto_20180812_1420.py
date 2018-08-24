# Generated by Django 2.0.6 on 2018-08-12 21:20

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0022_auto_20180725_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='intake_caseworker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intakes', to='cases.Person'),
        ),
        migrations.AlterField(
            model_name='case',
            name='incident_description',
            field=tinymce.models.HTMLField(),
        ),
    ]