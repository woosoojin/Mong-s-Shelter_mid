from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(blank=True, upload_to= "images/revewing")
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.title

class Question(models.Model):
    title2 = models.CharField(max_length = 100)
    description2 = models.CharField(max_length = 10000)

    def __str__(self):
        return self.title2

class Adopting(models.Model):
    name = models.CharField(max_length=255)
    name2 = models.CharField(blank=True, max_length=255)
    image = models.ImageField(blank=True, upload_to='images/adopting')
    image2 = models.ImageField(blank=True, upload_to='images/adopting')
    description = models.CharField(max_length=10000)
    description2 = models.CharField(blank=True, max_length=10000)

    
class School_parents(models.Model):
    title3 = models.CharField(max_length = 255)
    url1 = models.URLField(blank=True)
    description4 = models.CharField(max_length = 500)
    thumbnail = models.ImageField(blank=True, upload_to='images/school')

    def __str__(self):
        return self.title3

class School_dog(models.Model):
    title4 = models.CharField(max_length = 255)
    url2 = models.URLField(blank=True)
    description5 = models.CharField(max_length = 500)
    thumbnail2 = models.ImageField(blank=True, upload_to='images/school')

    def __str__(self):
        return self.title4
        
class Magazine(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 500)
    thumbnail = models.ImageField(blank=True, upload_to='images/magazine')