# Generated by Django 2.0.7 on 2018-07-18 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionnaire', '0003_variable_observation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variable',
            old_name='depuis_millesime',
            new_name='millesime',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='jusque_millesime',
        ),
    ]
