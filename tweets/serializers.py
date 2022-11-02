from rest_framework.serializers import ModelSerializer
from .models import Tweet


class TweetSerializer(ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('author', 'body', 'parent_tweet')