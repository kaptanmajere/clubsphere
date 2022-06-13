from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from clubs.models import Club, Post, Like


class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_clubAdmin = models.BooleanField(default=False)
    user_profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, null=True, blank=True)

    def save(self):
        super().save()
        if self.user_profile is None:
            self.user_profile = Profile.objects.create(user=self, first_name=self.first_name, last_name=self.last_name,
                                                       email=self.email)
            self.user_profile.save()
        super().save()


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    clubs = models.ManyToManyField(Club)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return f"{self.user.username}, {self.first_name}, {self.last_name}"
