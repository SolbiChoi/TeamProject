from django.db import models

# Create your models here.
class culture_scraping(models.Model):
    stargrade= models.TextField()
    review= models.TextField()

class fashion_scraping(models.Model):
    stargrade=models.TextField
    review=models.TextField

class food_scraping(models.Model):
    stargrade=models.TextField
    review=models.TextField

class living_scraping(models.Model):
    stargrade=models.TextField
    review=models.TextField

class tech_scraping(models.Model):
    stargrade=models.TextField
    review=models.TextField
