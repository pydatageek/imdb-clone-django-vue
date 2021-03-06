# Generated by Django 2.2.10 on 2020-04-03 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CelebComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField(auto_now_add=True, verbose_name='Added Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Added Date')),
                ('slug', models.SlugField(blank=True, max_length=10, unique=True, verbose_name='Slug')),
                ('text', models.CharField(max_length=250, verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'Celebrity Comment',
                'verbose_name_plural': 'Celebrity Comments',
            },
        ),
        migrations.CreateModel(
            name='MovieComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField(auto_now_add=True, verbose_name='Added Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Added Date')),
                ('slug', models.SlugField(blank=True, max_length=10, unique=True, verbose_name='Slug')),
                ('text', models.CharField(max_length=250, verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'Movie omment',
                'verbose_name_plural': 'Movie Comments',
            },
        ),
    ]
