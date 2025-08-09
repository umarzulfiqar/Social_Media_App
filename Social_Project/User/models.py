from django.db import models
from django.contrib.auth.models import User
import uuid
from PIL import Image

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars',default='default.jpg', blank=True,null=True)
    bio = models.TextField(blank=True, null= True)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        if not  self.avatar:
            self.avatar='default.jpg'
        super().save(*args, **kwargs)   #default save

        img=Image.open(self.avatar.path)   #open image from path

        if img.height > 300 or img.width > 300:   #check and resize image
            img.thumbnail((300, 300))
            img.save(self.avatar.path)
