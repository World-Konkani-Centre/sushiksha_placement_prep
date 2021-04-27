from django.db import models

class Question(models.Model):
    qno = models.IntegerField(default=0)
    text = models.CharField(max_length=45000)
    testcaseno = models.IntegerField(default=0)
    samplein = models.CharField(max_length=45000,default='')
    sampleout = models.CharField(max_length=45000,default='')
    tc1 = models.CharField(max_length=1000)
    tc2 = models.CharField(max_length=1000)
    tc3 = models.CharField(max_length=1000)
    tc1_sol = models.CharField(max_length=1000)
    tc2_sol = models.CharField(max_length=1000)
    tc3_sol = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.pk) 