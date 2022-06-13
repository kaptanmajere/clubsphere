from django.contrib import admin
from .models import Club, Post, Like, Comment,ParticipationState
# Register your models here.
from accounts.models import Profile

class ParticipationStateInline(admin.TabularInline):
    model = ParticipationState

class CommentInline(admin.TabularInline):
    model = Comment


class ProfileInline(admin.TabularInline):
    model = Profile.clubs.through


class PostInline(admin.TabularInline):
    model = Post


# inline for likes to Post
class LikeInline(admin.TabularInline):
    model = Like


# register Club
class ClubAdmin(admin.ModelAdmin):
    inlines = [ProfileInline, PostInline]


class PostAdmin(admin.ModelAdmin):
    inlines = [LikeInline, CommentInline, ParticipationStateInline]


admin.site.register(Club, ClubAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(ParticipationState)
