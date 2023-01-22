from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.NewPost)
admin.site.register(models.Comment)
