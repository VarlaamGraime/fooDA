from django.db import models

class Cuisine(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, related_name='dishes')
    ingredients = models.TextField()  # просто текст: "рис, мясо, лук"

    def __str__(self):
        return f"{self.name} ({self.cuisine.name})"

class DrinkCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Drink(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(DrinkCategory, on_delete=models.CASCADE, related_name='drinks')
    ingredients = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.category.name})"
