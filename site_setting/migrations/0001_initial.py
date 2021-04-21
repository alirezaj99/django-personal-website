# Generated by Django 3.1.6 on 2021-02-18 02:16

from django.db import migrations, models
import site_setting.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='تصویر پس زمینه', max_length=120, verbose_name='تصویر پس زمینه')),
                ('image', models.ImageField(blank=True, null=True, upload_to=site_setting.models.upload_image_path, verbose_name='عکس پروفایل')),
            ],
            options={
                'verbose_name': 'تصویر پس زمینه',
                'verbose_name_plural': 'تصاویر پس زمینه',
            },
        ),
    ]