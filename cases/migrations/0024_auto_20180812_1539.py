# Generated by Django 2.0.6 on 2018-08-12 22:39

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0023_auto_20180812_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='intake_caseworker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intakes', to='cases.Person'),
        ),
        migrations.AlterField(
            model_name='caseupdate',
            name='update_description',
            field=tinymce.models.HTMLField(),
        ),
    ]