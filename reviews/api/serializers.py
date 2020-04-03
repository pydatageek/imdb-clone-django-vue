from rest_framework import serializers

from reviews.models import CelebComment, MovieComment


class CelebCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CelebComment
        fields = ('text', 'celeb')


class MovieCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieComment
        fields = ('text', 'movie')
