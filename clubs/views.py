from .models import Club, Post, Like, Comment, ParticipationState
from rest_framework import viewsets
from rest_framework import permissions
from clubs.serializers import ClubSerializer, PostSerializer, LikeSerializer, CommentSerializer, ParticipationStateSerializer

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClubSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

class ParticipationStateViewSet(viewsets.ModelViewSet):
    queryset = ParticipationState.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ParticipationStateSerializer

