from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


#User app models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(default='users/default.jpg', upload_to='users/profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)                
        output_size = (50, 50)
        img.thumbnail(output_size)
        img.save(self.image.path)