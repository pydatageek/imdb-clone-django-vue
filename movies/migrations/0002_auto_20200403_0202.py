# Generated by Django 2.2.10 on 2020-04-03 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('celebs', '0002_auto_20200403_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='pgrating',
            name='added_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies_pgrating_adders', to=settings.AUTH_USER_MODEL, verbose_name='Added By'),
        ),
        migrations.AddField(
            model_name='pgrating',
            name='modified_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies_pgrating_modifiers', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='moviecrew',
            name='crew',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moviecrews', to='celebs.Celebrity', verbose_name='Crew'),
        ),
        migrations.AddField(
            model_name='moviecrew',
            name='duty',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='moviecrews', to='celebs.Duty', verbose_name='Duty'),
        ),
        migrations.AddField(
            model_name='moviecrew',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moviecrews', to='movies.Movie', verbose_name='Movie'),
        ),
        migrations.AddField(
            model_name='movie',
            name='added_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies_movie_adders', to=settings.AUTH_USER_MODEL, verbose_name='Added By'),
        ),
        migrations.AddField(
            model_name='movie',
            name='crews',
            field=models.ManyToManyField(related_name='movies', through='movies.MovieCrew', to='celebs.Celebrity', verbose_name='Crews'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='movies', to='movies.Genre', verbose_name='Genres'),
        ),
        migrations.AddField(
            model_name='movie',
            name='modified_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies_movie_modifiers', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AddField(
            model_name='movie',
            name='pg_rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies', to='movies.PgRating', verbose_name='PG Rating'),
        ),
        migrations.AddField(
            model_name='genre',
            name='added_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies_genre_adders', to=settings.AUTH_USER_MODEL, verbose_name='Added By'),
        ),
        migrations.AddField(
            model_name='genre',
            name='modified_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies_genre_modifiers', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
    ]
