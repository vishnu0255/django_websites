from django.db import models
from datetime import date
from  django.utils.timezone import now

# Create your models here.
class NewPost(models.Model):
    post_author = models.CharField(max_length=20)
    post_title = models.CharField(max_length=32)
    post_text = models.CharField(max_length=200)
    post_save = models.BooleanField(default=False)
    post_time = models.DateField(max_length=200,default=now,null=True)

    def __str__(self):
        return self.post_title

class Comment(models.Model):
    post_comments = models.CharField(max_length=1000)
    post_title = models.CharField(max_length=32)
    post_id       = models.IntegerField(null=True)
    post_comment_author = models.CharField(max_length=50)
    comment_approve = models.BooleanField(default=False)
    comment_time = models.DateField(max_length=200,default=now,null=True)

    def __str__(self):
        return self.post_comments
