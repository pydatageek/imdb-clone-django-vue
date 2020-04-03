from rest_framework import serializers

from movies.models import Genre, PgRating, Movie, MovieCrew


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'slug', 'content',)
        lookup_field = 'slug'


class PgRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PgRating
        fields = ('id', 'name', 'code', 'slug', 'content')
        lookup_field = 'slug'


class MovieSerializer(serializers.ModelSerializer):
    pg_rating = serializers.SerializerMethodField()
    image_name = serializers.SerializerMethodField()
    image_thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = (
            'id', 'name', 'slug',
            'release_year', 'duration', 'imdb_rating', 'pg_rating',
            'content', 'source_content', 'trailer',
            'image', 'image_name', 'image_thumbnail', 'credit_image',
            'genres', 'crews', 'youtube_video')
        lookup_field = 'slug'

    def get_pg_rating(self, obj):
        if obj.pg_rating:
            return {
                'id': obj.pg_rating.id,
                'name': obj.pg_rating.name,
                'code': obj.pg_rating.code
            }
        return ''

    def get_image_name(self, obj):
        if obj.image and hasattr(obj.image, 'name'):
            return obj.image.name
        return ''

    def get_image_thumbnail(self, obj):
        return obj.image_thumbnail.url


class MovieCrewSerializer(serializers.ModelSerializer):
    duty = serializers.SerializerMethodField()
    movie = serializers.SerializerMethodField()
    crew = serializers.SerializerMethodField()

    class Meta:
        model = MovieCrew
        fields = ('id', 'duty', 'movie', 'crew', 'role', 'screen_name')
        lookup_field = 'slug'

    def get_duty(self, obj):
        if obj.duty:
            return {
                'id': obj.duty.id, 'code': obj.duty.code, 'name': obj.duty.name
            }
        return ''

    def get_movie(self, obj):
        if obj.movie:
            return {
                'id': obj.movie.id, 'slug': obj.movie.slug, 'name': obj.movie.name
            }
        return ''

    def get_crew(self, obj):
        if obj.crew:
            return {
                'id': obj.crew.id, 'slug': obj.crew.slug, 'name': obj.crew.full_name
            }
        return ''
