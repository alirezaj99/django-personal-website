# Generated by Django 3.1.6 on 2021-02-18 05:59

from django.db import migrations, models
import site_setting.models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='عنوان سایت', max_length=120, verbose_name='عنوان سایت')),
                ('icon', models.ImageField(blank=True, null=True, upload_to=site_setting.models.upload_image_path_icon, verbose_name='عکس پروفایل')),
                ('footer', models.CharField(default='فوتر سایت', max_length=250, verbose_name='فوتر سایت')),
            ],
            options={
                'verbose_name': 'آیکون سایت و فوتر',
                'verbose_name_plural': 'آیکون های سایت و فوتر',
            },
        ),
    ]
