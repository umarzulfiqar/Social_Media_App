from django.db import models
from django.contrib.auth.models import User
import uuid
from PIL import Image

class Post(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    post_content = models.TextField(null=False)
    post_image = models.ImageField(upload_to="posts",null=True,blank=True)
    post_user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
#Resizing Image
        if self.post_image:
            img_path = self.post_image.path
            img = Image.open(img_path)
            max_size = (800, 800)
            img.thumbnail(max_size)
            img.save(img_path)

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add = True)

class Like(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post','user')