from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
      return self.name

class Categories(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='categories')
    tops = models.CharField(max_length=200)
    bottoms = models.CharField(max_length=200)
    shoes = models.CharField(max_length=200)
    accessories = models.CharField(max_length=200)

    def __str__(self):
      return self.name

class Activities(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='activites')
    name = models.CharField(max_length=200)
    description = models.TextField()
    free = models.BooleanField()
    indoors = models.BooleanField()

    def __str__(self):
      return self.name

class Items(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='items')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='items')
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