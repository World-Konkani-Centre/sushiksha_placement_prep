from django.db import models
from ckeditor.fields import RichTextField

DIFF_OPTION = (
    ("1", "Easy"),
    ("2", "Medium"),
    ("3", "Hard"),
)


class DSACategory(models.Model):
    name = models.TextField(max_length=100, help_text="Category name")

    def __str__(self):
        return f'{self.name}'


class SubCategory(models.Model):
    category = models.ForeignKey(DSACategory, on_delete=models.SET_NULL, null=True)
    sub_name = models.TextField(max_length=100, help_text="Category name ")


class Question(models.Model):
    sub_cat = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    difficulty = models.TextField(max_length=2, choices=DIFF_OPTION, default="1")
    name = models.TextField(max_length=100)
    text = RichTextField(verbose_name="Description of the question",
                         blank=False, help_text="a description of the question")
    samplein = models.CharField(max_length=45000, default='')
    sampleout = models.CharField(max_length=45000, default='')
    tc = models.TextField(null=True, blank=True)
    tc_sol = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.pk)
