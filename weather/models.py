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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items', null=True)
    name = models.CharField(max_length=200, default="no name", null=True)
    description = models.TextField(default="no description", null=True)
    photo = models.CharField(max_length=500, default="no photo", null=True)
    hot = models.BooleanField(default=False, null=True)
    warm = models.BooleanField(default=False, null=True)
    cool = models.BooleanField(default=False, null=True)
    cold = models.BooleanField(default=False, null=True)
    rain = models.BooleanField(default=False, null=True)
    snow = models.BooleanField(default=False, null=True)
    wind = models.BooleanField(default=False, null=True)

    def __str__(self):
      return self.name