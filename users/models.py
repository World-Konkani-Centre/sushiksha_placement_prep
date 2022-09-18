from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from sushiksha_placement_prep.settings import APTITUDE_BADGE_ID, RESUME_BADGE_ID, HR_BADGE_ID, GD_BADGE_ID, \
    TECHNICAL_BADGE_ID

ATTEMPTED_BADGE_ID = 7

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/%Y/%m/')
    is_mentor = models.BooleanField(default=False)
    batch = models.IntegerField(default=2018)
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

    
    
    def check_for_apti(self):
        if len(self.reward_set.filter(badge__id=APTITUDE_BADGE_ID, user=self)) == 0:
            return False
        else:
            return True

    def check_for_resume(self):
        if len(self.reward_set.filter(badge__id=RESUME_BADGE_ID, user=self)) == 0:
            return False
        else:
            return True

    def check_for_tech(self):
        if len(self.reward_set.filter(badge__id=TECHNICAL_BADGE_ID, user=self)) == 0:
            return False
        else:
            return True

    def check_for_gd(self):
        if len(self.reward_set.filter(badge__id=GD_BADGE_ID, user=self)) == 0:
            return False
        else:
            return True

    def check_for_attempted(self):
        if len(self.reward_set.filter(badge__id=ATTEMPTED_BADGE_ID, user=self)) == 0:
            return False
        else:
            return True

    def check_for_attempted_tech(self):
        if len(self.reward_set.filter(badge__id=ATTEMPTED_BADGE_ID, user=self)) == 0:
            return False
        elif self.reward_set.filter(badge__id=ATTEMPTED_BADGE_ID, user=self).first().description != 'tech':
            return True

    def check_for_attempted_hr(self):
        if len(self.reward_set.filter(badge__id=ATTEMPTED_BADGE_ID, user=self)) == 0:
            return False
        elif self.reward_set.filter(badge__id=ATTEMPTED_BADGE_ID, user=self).first().description != 'hr':
            return True

    def check_for_hr(self):
        if len(self.reward_set.filter(badge__id=HR_BADGE_ID, user=self)) == 0:
            return False
        else:
            return True


    def url_for_hr(self):
        return self.reward_set.filter(badge__id=HR_BADGE_ID).first().badge.image.url

    def url_for_tech(self):
        return self.reward_set.filter(badge__id=TECHNICAL_BADGE_ID).first().badge.image.url

    def url_for_resume(self):
        return self.reward_set.filter(badge__id=RESUME_BADGE_ID).first().badge.image.url

    def url_for_apti(self):
        return self.reward_set.filter(badge__id=APTITUDE_BADGE_ID).first().badge.image.url

    def url_for_gd(self):
        return self.reward_set.filter(badge__id=GD_BADGE_ID).first().badge.image.url

    def url_for_attempted(self):
        return self.reward_set.filter(badge__id=ATTEMPTED_BADGE_ID).first().badge.image.url
