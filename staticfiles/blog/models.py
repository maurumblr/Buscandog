from email.policy import default
from tokenize import blank_re
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='posts/posts_image', blank=True)
    image2 = models.ImageField(upload_to='posts/posts_image', blank=True)
    image3 = models.ImageField(upload_to='posts/posts_image', blank=True)

    def get_absolute_url(self):
        return reverse('blog-detail-post', kwargs={'pk': self.pk})