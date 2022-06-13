from django.db import models


# import Custom user from accounts


# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to='club_pictures/', blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/', blank=True)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    attendee_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    def save(self):
        self.like_count = Like.objects.filter(post=self).count()
        print(Like.objects.filter(post=self).count())
        self.comment_count = Comment.objects.filter(post=self).count()
        self.attendee_count = ParticipationState.objects.filter(post=self).count()
        super().save()

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)

    class Meta:
        unique_together = ('post', 'user',)

    def __str__(self):
        return self.user



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        unique_together = ('post', 'user',)



class ParticipationState(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user

    class Meta:
        unique_together = ('post', 'user',)
