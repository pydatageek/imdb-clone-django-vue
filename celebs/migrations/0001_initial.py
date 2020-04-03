# Generated by Django 2.2.10 on 2020-04-03 02:02

import celebs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField(auto_now_add=True, verbose_name='Added Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Added Date')),
                ('slug', models.SlugField(blank=True, max_length=160, unique=True, verbose_name='Slug')),
                ('first_name', models.CharField(max_length=75, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=75, verbose_name='Last Name')),
                ('nick_name', models.CharField(blank=True, default='', max_length=50, verbose_name='Nick Name')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('birth_place', models.CharField(blank=True, default='', max_length=100, verbose_name='Birth Place')),
                ('content', models.TextField(blank=True, default='', verbose_name='Biography')),
                ('source_content', models.URLField(blank=True, default='', verbose_name='Biography Souce')),
                ('trailer', models.URLField(blank=True, default='', help_text='trailer url (ONLY for youtube videos yet)', verbose_name='Trailer')),
                ('image', models.ImageField(blank=True, default='celebs/default_celeb.jpg', null=True, upload_to=celebs.models.celeb_directory_path, verbose_name='Image')),
                ('credit_image', models.CharField(blank=True, default='', max_length=250, verbose_name='Image Credit')),
            ],
            options={
                'verbose_name': 'Celebrity',
                'verbose_name_plural': 'Celebrities',
                'ordering': ('last_name', 'first_name'),
            },
        ),
        migrations.CreateModel(
            name='CelebrityDuty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Celebrity Duty',
                'verbose_name_plural': 'Celebrity Duties',
            },
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField(auto_now_add=True, verbose_name='Added Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Added Date')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, max_length=110, unique=True, verbose_name='Slug')),
                ('code', models.CharField(max_length=1, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Duty',
                'verbose_name_plural': 'Duties',
                'ordering': ('code',),
            },
        ),
    ]