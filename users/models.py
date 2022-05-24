from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

#User app models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(default='users/default.jpg', upload_to='users/profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'