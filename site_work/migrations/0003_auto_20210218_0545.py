# Generated by Django 3.1.6 on 2021-02-18 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_work', '0002_work_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Work',
            new_name='Works',
        ),
    ]