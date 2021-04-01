from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    role = models.BooleanField(default=False)
    name = models.CharField(max_length=100, default=None, blank=True, null=True)


    def __str__(self):
        return f"{self.user.username}"
