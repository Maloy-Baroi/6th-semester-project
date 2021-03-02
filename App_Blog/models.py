from django.db import models
from App_login.models import CustomUser


# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(CustomUser, related_name='post_author', on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=254, verbose_name='Put a Title')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    blog_content = models.TextField(verbose_name="What's on your mind")
    blog_image = models.ImageField(upload_to='blog_images', verbose_name='Image')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.blog_title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return self.comment


class Likes(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='liked_blog')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='liked_user')

    def __str__(self):
        return str(self.user) + " Likes" + str(self.blog)
