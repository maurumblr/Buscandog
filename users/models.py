from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.files.storage import default_storage as storage

#User email field unique
User._meta.get_field('email')._unique = True


#User app models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='users/profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)        

        image = Image.open(self.image)        
        resized_image = image.resize((75, 75), Image.ANTIALIAS)
        fh = storage.open(self.image.name, "w")
        picture_format = 'png'
        resized_image.save(fh, picture_format)
        fh.close()
        # resized_image.save(self.image.path)
        return user