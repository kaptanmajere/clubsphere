from .models import Club, Post, Like, Comment, ParticipationState
from rest_framework import serializers

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ParticipationStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipationState
        fields = '__all__'
