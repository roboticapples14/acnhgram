from django.db import models

# Create your models here.
class ShowcasePost(models.Model):
  name = models.CharField(max_length= 100)
  image = models.URLField(help_text="Enter a URL pointing to your image")
  description = models.TextField(max_length= 500)
  species = models.CharField(max_length=100, help_text='The animal type of the villager.')
  teir = models.CharField(help_text='The teir of the villager (S, A, B, C, D).', max_length = 1)
  personality = models.CharField(max_length=200)
