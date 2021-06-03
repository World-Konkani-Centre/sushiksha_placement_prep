from django.contrib.auth.models import User
from django.db import models

OPTIONS = (
    ('HR', 'HR'),
    ('Technical', 'Technical'),
    ('Counselling', 'Counselling'),
)

class Branch(models.Model):
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.branch


class Interview(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=50, choices=OPTIONS, default="Technical")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    link = models.URLField(default='https://tinyurl.com/sushiksha-meet')
    participant_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='part1', null=True)
    participant_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='part2', null=True, blank=True)
    complete = models.BooleanField(default=False)
    event_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.branch} - {self.type} - {self.participant_1}'


class GD(models.Model):
    heading = models.CharField(max_length=50)
    count = models.IntegerField(default=1)
    participant_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='part_1', null=True)
    participant_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='part_2', null=True, blank=True)
    participant_3 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='part_3', null=True, blank=True)
    participant_4 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='part_4', null=True, blank=True)
    participant_5 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='part_5', null=True, blank=True)
    participant_6 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='part_6', null=True, blank=True)
    participant_7 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='part_7', null=True, blank=True)
    participant_8 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='part_8', null=True, blank=True)
    participant_9 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='part_9', null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    link = models.URLField(default='https://tinyurl.com/pair-link')
    complete = models.BooleanField(default=False)
    event_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.heading} - {self.participant_1}'
