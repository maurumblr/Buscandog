from pyexpat import model
from django.contrib import admin
from . import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'date', 'creator']
    ordering = ['date']
    list_filter = ['creator',]


admin.site.register(models.Post, PostAdmin)