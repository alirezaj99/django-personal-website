# Generated by Django 3.1.6 on 2021-02-17 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(default='مکان تحصیل', max_length=300, verbose_name='مکان تحصیل')),
                ('time', models.CharField(default='بازه زمان تحصیل', max_length=100, verbose_name='بازه زمان تحصیل')),
                ('description', models.CharField(default='توضیحات تحصیل', max_length=400, verbose_name='توضیحات تحصیل')),
                ('active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'تحصیل من',
                'verbose_name_plural': 'تحصیلات من',
            },
        ),
        migrations.CreateModel(
            name='ResumeExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='عنوان تجربه', max_length=300, verbose_name='عنوان تجربه')),
                ('time', models.CharField(default='بازه زمان تجربه', max_length=100, verbose_name='بازه زمان تجربه')),
                ('description', models.CharField(default='توضیحات تجربه', max_length=400, verbose_name='توضیحات تجربه')),
                ('active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'تجربه من',
                'verbose_name_plural': 'تجربه های من',
            },
        ),
        migrations.CreateModel(
            name='ResumeSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='عنوان مهارت من', max_length=100, verbose_name='عنوان مهارت من')),
                ('percent', models.IntegerField(default=0, verbose_name='درصد مهارت')),
                ('active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'مهارت من',
                'verbose_name_plural': 'مهارت های من',
            },
        ),
    ]
