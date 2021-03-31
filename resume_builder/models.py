from django.contrib.auth.models import User
from django.db import models

STATUS = (
    ('1', 'Queued'),
    ('2', 'Reviewed'),
    ('3', 'Complete'),
)


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    CV = models.FileField()
    status = models.CharField(max_length=3, choices=STATUS, default='1')


class Comments(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
