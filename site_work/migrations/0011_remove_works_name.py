# Generated by Django 3.1.6 on 2021-03-31 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_work', '0010_works_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='works',
            name='name',
        ),
    ]
