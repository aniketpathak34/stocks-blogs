from email import header
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from ckeditor.fields import RichTextField



# Create your models here.
class StockDetail(models.Model):
    stock = models.CharField(max_length=255, unique=True)
    user = models.ManyToManyField(User)


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=200, null=True, blank=True )
    facebook_url = models.CharField(max_length=200, null=True, blank=True )
    instagram_url = models.CharField(max_length=200, null=True, blank=True )
    linkedin_url = models.CharField(max_length=200, null=True, blank=True )

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        # return reverse('post_detail', args=[str(self.slug)])
        return reverse ('home1')

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='mainapp')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextField(blank=True, null=True)
    # content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('post_detail', args=[str(self.slug)])
        return reverse ('home1')


class Comment(models.Model):
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)
