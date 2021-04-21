# Generated by Django 3.1.6 on 2021-02-18 02:20

from django.db import migrations, models
import django.utils.timezone
import site_work.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('site_work', '0004_delete_works'),
    ]

    operations = [
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='تصویر', max_length=100, verbose_name='تصویر')),
                ('description', models.CharField(default='توضیحات', max_length=250, verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, null=True, upload_to=site_work.models.upload_image_path, verbose_name='تصویر کار')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
            ],
            options={
                'verbose_name': 'کار',
                'verbose_name_plural': 'کارها',
            },
        ),
    ]