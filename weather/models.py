from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
      return self.name

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=200)

    def __str__(self):
      return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activites')
    name = models.CharField(max_length=200)
    description = models.TextField()
    free = models.BooleanField()
    indoors = models.BooleanField()

    def __str__(self):
      return self.name

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.CharField(max_length=500)
    hot = models.BooleanField()
    warm = models.BooleanField()
    cool = models.BooleanField()
    cold = models.BooleanField()
    rain = models.BooleanField()
    snow = models.BooleanField()
    wind = models.BooleanField()

    def __str__(self):
      return self.name