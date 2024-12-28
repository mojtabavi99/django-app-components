# Generated by Django 5.1.4 on 2024-12-28 19:55

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='عنوان سایت')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام سایت')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوضیحات سایت')),
                ('slogan', models.CharField(blank=True, max_length=255, null=True, verbose_name='شعار سایت')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='ایمیل')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='تلفن')),
                ('mobile', models.CharField(blank=True, max_length=255, null=True, verbose_name='موبایل')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='آدرس')),
                ('instagram', models.CharField(blank=True, max_length=255, null=True, verbose_name='اینستاگرام')),
                ('facebook', models.CharField(blank=True, max_length=255, null=True, verbose_name='فیسبوک')),
                ('telegram', models.CharField(blank=True, max_length=255, null=True, verbose_name='تلگرام')),
                ('twitter', models.CharField(blank=True, max_length=255, null=True, verbose_name='توییتر')),
                ('whatsapp', models.CharField(blank=True, max_length=255, null=True, verbose_name='واتساپ')),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True, verbose_name='لینکدین')),
                ('youtube', models.CharField(blank=True, max_length=255, null=True, verbose_name='یوتیوب')),
                ('aparat', models.CharField(blank=True, max_length=255, null=True, verbose_name='آپارات')),
                ('logo', models.ImageField(blank=True, default='images/core/config/default.png', null=True, upload_to='images/core/config/', validators=[django.core.validators.FileExtensionValidator(['png'])], verbose_name='لوگو')),
            ],
            options={
                'verbose_name': 'تنظیمات',
                'verbose_name_plural': 'تنظیمات',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام استان')),
                ('country', models.CharField(default='ایران', max_length=255, verbose_name='کشور')),
                ('countrycode', models.IntegerField(default=98, verbose_name='کد کشور')),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True, verbose_name='latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True, verbose_name='longitude')),
                ('image', models.ImageField(blank=True, default='images/core/province/default.png', null=True, upload_to='images/core/province/', validators=[django.core.validators.FileExtensionValidator(['png, jpg, jpeg, webp'])], verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'استان',
                'verbose_name_plural': 'استان\u200cها',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام شهر')),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True, verbose_name='latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True, verbose_name='longitude')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_core.province', verbose_name='شناسه استان')),
            ],
            options={
                'verbose_name': 'شهر',
                'verbose_name_plural': 'شهرها',
            },
        ),
    ]
