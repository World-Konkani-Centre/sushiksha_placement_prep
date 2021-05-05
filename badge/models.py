from django.db import models
from users.models import Profile


class BadgeCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Badge(models.Model):
    points = models.IntegerField(default=1)
    title = models.CharField(max_length=50, help_text='Provide the title of the Badge')
    category = models.ForeignKey(BadgeCategory, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200, help_text='Reason to give this Badge')
    image = models.ImageField(upload_to='badges')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    

class Reward(models.Model):
    awarded_by = models.CharField(max_length=50, default='admin')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    descritpion = models.TextField()
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.awarded_by} Awarded a Badge to {self.user.name}'
    

