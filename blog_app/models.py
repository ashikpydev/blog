from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ForeignKey
# Create your models here.

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name = 'user_profile', on_delete=models.CASCADE )
    # profile_pic = models.ImageField(upload_to='profile_pics')
    profile_pic = models.FileField(upload_to="profile_pics", blank=True, null=True)

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'post_author')
    blog_title = models.CharField(max_length=250, verbose_name="Put a Title", blank = True, null = True)
    slug = models.SlugField(max_length=264, unique= True)
    blog_content = models.TextField(blank=True, null=True, verbose_name= "what is on your mind")
    blog_image = models.ImageField(upload_to='blog_images', verbose_name="Image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='user_comment')
    comment = models.TextField(blank=True, null = True)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=CASCADE, related_name='blog_liked')
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='blog_liked')
        
        
