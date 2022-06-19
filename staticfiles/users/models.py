from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.files.storage import default_storage as storage
from io import BytesIO


#User app models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='users/profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)                
    #     output_size = (50, 50)
    #     img.thumbnail(output_size)
    #     img.save(self.image.name)

    # def save(self, *args, **kwargs):
    #     #run save of parent class above to save original image to disk
    #     super().save(*args, **kwargs)

    #     memfile = BytesIO()

    #     img = Image.open(self.image)        
    #     output_size = (65, 65)
    #     img.thumbnail(output_size, Image.ANTIALIAS)
    #     img_rgb = img.convert('RGB')
    #     img_rgb.save(memfile, 'JPEG', quality=95)
    #     default_storage.save(self.image.name, memfile)
    #     memfile.close()
    #     img.close()

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