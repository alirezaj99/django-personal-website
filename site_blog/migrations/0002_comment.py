# Generated by Django 3.1.6 on 2021-02-17 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='نام')),
                ('text', models.TextField(verbose_name='نظر')),
                ('email', models.EmailField(max_length=100, verbose_name='ایمیل')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')),
                ('active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='site_blog.blogs', verbose_name='بلاگ')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
            },
        ),
    ]
