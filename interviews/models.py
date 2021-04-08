from django.contrib.auth.models import User
from django.db import models


class Interview(models.Model):
    heading = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    link = models.URLField(default='https://tinyurl.com/pair-link')
    participant_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='part1', null=True)
    participant_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='part2', null=True, blank=True)
    complete = models.BooleanField(default=False)
