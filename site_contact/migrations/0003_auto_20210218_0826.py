# Generated by Django 3.1.6 on 2021-02-18 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_contact', '0002_auto_20210218_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='خوانده شده / نشده'),
        ),
    ]
