from django.contrib.auth.models import User
from django.db import models

OPTIONS = (
    ('HR', 'HR'),
    ('Technical', 'Technical')
)


class Interview(models.Model):
    heading = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=OPTIONS, default="Technical")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    link = models.URLField(default='https://tinyurl.com/pair-link')
    participant_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='part1', null=True)
    participant_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='part2', null=True, blank=True)
    complete = models.BooleanField(default=False)
    event_id = models.CharField(max_length=50, null=True, blank=True)


class GDParticipants(models.Model):
    participants = models.ForeignKey(User, on_delete=models.CASCADE)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.participants.profile.name}'


class GDList(models.Model):
    participants = models.CharField(max_length=300)
    heading = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    link = models.URLField()
    complete = models.BooleanField(default=False)
    event_id = models.CharField(max_length=50)
