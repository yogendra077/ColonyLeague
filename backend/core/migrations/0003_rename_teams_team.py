# Generated by Django 4.2 on 2023-04-07 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_teams'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Teams',
            new_name='Team',
        ),
    ]
