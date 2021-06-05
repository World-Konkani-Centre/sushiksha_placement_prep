from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from datetime import datetime




# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/%Y/%m/')
    is_mentor = models.BooleanField(default=False)
    name = models.CharField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        

        img = Image.open(self.image.path)

        img_width, img_height = img.size

        output_size = (500, 500)
        box = ((img_width - min(img.size)) // 2, (img_height - min(img.size)) // 2, (img_width + min(img.size)) // 2, (img_height + min(img.size)) // 2)
        img = img.crop(box)
        img.thumbnail(output_size)
        img.save(self.image.path)

