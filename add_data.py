from webapp.models import Cuisine, DrinkCategory, Dish, Drink
from webapp.models import Dish, Drink, Cuisine, DrinkCategory

# Кухни
rus = Cuisine.objects.get_or_create(name="Русская")[0]
ita = Cuisine.objects.get_or_create(name="Итальянская")[0]
med = Cuisine.objects.get_or_create(name="Средиземноморская")[0]
amer = Cuisine.objects.get_or_create(name="Американская")[0]
fra = Cuisine.objects.get_or_create(name="Французская")[0]

# Категории напитков
hot = DrinkCategory.objects.get_or_create(name="Горячие")[0]
cold = DrinkCategory.objects.get_or_create(name="Холодные")[0]

# Блюда
Dish.objects.get_or_create(name="Борщ", cuisine=rus, ingredients="свекла, капуста, мясо")
Dish.objects.get_or_create(name="Окрошка", cuisine=rus, ingredients="кефир, огурцы, картофель")
Dish.objects.get_or_create(name="Пицца Маргарита", cuisine=ita, ingredients="тесто, томатный соус, моцарелла")
Dish.objects.get_or_create(name="Спагетти Болоньезе", cuisine=ita, ingredients="спагетти, мясной соус")
Dish.objects.get_or_create(name="Греческий салат", cuisine=med, ingredients="огурцы, помидоры, фета, маслины")
Dish.objects.get_or_create(name="Чизбургер", cuisine=amer, ingredients="булка, котлета, сыр, огурцы")
Dish.objects.get_or_create(name="Рататуй", cuisine=fra, ingredients="баклажаны, цукини, помидоры")

# Напитки
Drink.objects.get_or_create(name="Чай", category=hot, ingredients="вода, чай")
Drink.objects.get_or_create(name="Кофе", category=hot, ingredients="вода, кофе")
Drink.objects.get_or_create(name="Лимонад", category=cold, ingredients="вода, лимон, сахар")
Drink.objects.get_or_create(name="Компот", category=cold, ingredients="вода, ягоды")
Drink.objects.get_or_create(name="Какао", category=hot, ingredients="молоко, какао")
Drink.objects.get_or_create(name="Мохито", category=cold, ingredients="мята, лайм, газировка")
