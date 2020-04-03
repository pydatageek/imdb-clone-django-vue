from rest_framework import serializers

from movies.models import MovieCrew
from celebs.models import (Duty, Celebrity, CelebrityDuty)


class DutySerializer(serializers.ModelSerializer):
    class Meta:
        model = Duty
        fields = ('id', 'code', 'name', 'slug')
        lookup_field = 'slug'


class CelebritySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    image_name = serializers.SerializerMethodField()
    image_thumbnail = serializers.SerializerMethodField()
    # duties = serializers.SerializerMethodField()

    class Meta:
        model = Celebrity
        fields = (
            'id', 'slug', 'name', 'last_name', 'nick_name', 'full_name',
            'birth_date', 'birth_place', 'age',
            'youtube_video', 'trailer', 'duties',
            'content', 'source_content',
            'image', 'image_name', 'image_thumbnail', 'credit_image')
        lookup_field = 'slug'

    def get_name(self, obj):
        return obj.first_name

    def get_image_name(self, obj):
        if obj.image and hasattr(obj.image, 'name'):
            return obj.image.name
        return ''

    def get_image_thumbnail(self, obj):
        return obj.image_thumbnail.url

    # def get_duties(self, obj):
    #     duty_list = []
    #     if obj.duties:
    #         for duty in obj.duties.all():
    #             duty_list.append({
    #                 'id': duty.id, 'code': duty.code, 'name': duty.name
    #             })
    #     return duty_list


class MovieCrewSerializer(serializers.ModelSerializer):
    duty = serializers.SerializerMethodField()
    movie = serializers.SerializerMethodField()
    crew = serializers.SerializerMethodField()

    class Meta:
        model = MovieCrew
        fields = ('id', 'duty', 'movie', 'crew', 'role', 'screen_name')

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
