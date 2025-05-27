from webapp.models import Cuisine, DrinkCategory, Dish, Drink

rus = Cuisine.objects.get_or_create(name="Русская")[0]
cat = DrinkCategory.objects.get_or_create(name="Горячие")[0]

Dish.objects.create(name="Борщ", cuisine=rus, ingredients="свекла, капуста, мясо")
Drink.objects.create(name="Чай", category=cat, ingredients="вода, чай")
