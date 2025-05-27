from webapp.models import Cuisine, DrinkCategory, Dish, Drink
from webapp.models import Dish, Drink, Cuisine, DrinkCategory

# Кухни
rus = Cuisine.objects.get_or_create(name="Русская")[0]
asia = Cuisine.objects.get_or_create(name="Азиатская")[0]
fra = Cuisine.objects.get_or_create(name="Французская")[0]
ita = Cuisine.objects.get_or_create(name="Итальянская")[0]
mex = Cuisine.objects.get_or_create(name="Мексиканская")[0]
ind = Cuisine.objects.get_or_create(name="Индийская")[0]
amer = Cuisine.objects.get_or_create(name="Американская")[0]
med = Cuisine.objects.get_or_create(name="Средиземноморская")[0]
scand = Cuisine.objects.get_or_create(name="Скандинавская")[0]

# Категории напитков
hot = DrinkCategory.objects.get_or_create(name="Горячие")[0]
cold = DrinkCategory.objects.get_or_create(name="Холодные")[0]
coffee = DrinkCategory.objects.get_or_create(name="Кофейные")[0]
sugarfree = DrinkCategory.objects.get_or_create(name="Без сахара")[0]

# Блюда
Dish.objects.get_or_create(name="Борщ", cuisine=rus, ingredients="свекла, капуста, картофель, мясо, томат")
Dish.objects.get_or_create(name="Пельмени", cuisine=rus, ingredients="фарш, мука, лук, специи")
Dish.objects.get_or_create(name="Окрошка", cuisine=rus, ingredients="кефир, огурцы, яйца, картофель, зелень")
Dish.objects.get_or_create(name="Гречневая каша", cuisine=rus, ingredients="гречка, масло, соль")
Dish.objects.get_or_create(name="Селедка под шубой", cuisine=rus, ingredients="сельдь, картофель, свекла, морковь, майонез")
Dish.objects.get_or_create(name="Щи", cuisine=rus, ingredients="капуста, морковь, картофель, мясо")
Dish.objects.get_or_create(name="Блины", cuisine=rus, ingredients="мука, молоко, яйца, сахар")
Dish.objects.get_or_create(name="Голубцы", cuisine=rus, ingredients="капуста, рис, мясо, лук")
Dish.objects.get_or_create(name="Вареники с вишней", cuisine=rus, ingredients="мука, вишня, сахар")
Dish.objects.get_or_create(name="Котлета по-киевски", cuisine=rus, ingredients="куриное филе, масло, панировка")

Dish.objects.get_or_create(name="Суши", cuisine=asia, ingredients="рис, рыба, нори, уксус")
Dish.objects.get_or_create(name="Лапша удон", cuisine=asia, ingredients="удон, овощи, соевый соус")
Dish.objects.get_or_create(name="Том Ям", cuisine=asia, ingredients="креветки, лимонграсс, кокосовое молоко, грибы")
Dish.objects.get_or_create(name="Кимчи", cuisine=asia, ingredients="пекинская капуста, чеснок, чили, имбирь")
Dish.objects.get_or_create(name="Рамен", cuisine=asia, ingredients="лапша, бульон, мясо, яйцо, водоросли")
Dish.objects.get_or_create(name="Терияки курица", cuisine=asia, ingredients="курица, терияки, кунжут, рис")
Dish.objects.get_or_create(name="Мисо суп", cuisine=asia, ingredients="мисо паста, тофу, нори, лук")
Dish.objects.get_or_create(name="Спринг-роллы", cuisine=asia, ingredients="рисовая бумага, овощи, креветки")
Dish.objects.get_or_create(name="Чоу мейн", cuisine=asia, ingredients="лапша, говядина, соус, овощи")
Dish.objects.get_or_create(name="Темпура", cuisine=asia, ingredients="овощи, кляр, соус")

Dish.objects.get_or_create(name="Рататуй", cuisine=fra, ingredients="кабачки, баклажаны, помидоры, перец")
Dish.objects.get_or_create(name="Круассаны", cuisine=fra, ingredients="мука, масло, дрожжи, сахар")
Dish.objects.get_or_create(name="Луковый суп", cuisine=fra, ingredients="лук, бульон, сыр, хлеб")
Dish.objects.get_or_create(name="Киш Лорен", cuisine=fra, ingredients="яйца, сливки, сыр, бекон")
Dish.objects.get_or_create(name="Фондю", cuisine=fra, ingredients="сыр, белое вино, хлеб")
Dish.objects.get_or_create(name="Биф Бургиньон", cuisine=fra, ingredients="говядина, вино, грибы, морковь")
Dish.objects.get_or_create(name="Конфи из утки", cuisine=fra, ingredients="утка, жир, чеснок")
Dish.objects.get_or_create(name="Крем-брюле", cuisine=fra, ingredients="сливки, ваниль, сахар")
Dish.objects.get_or_create(name="Тарт Татен", cuisine=fra, ingredients="яблоки, тесто, масло, сахар")
Dish.objects.get_or_create(name="Гратен", cuisine=fra, ingredients="картофель, сливки, сыр")

Dish.objects.get_or_create(name="Пицца Маргарита", cuisine=ita, ingredients="тесто, томаты, моцарелла, базилик")
Dish.objects.get_or_create(name="Паста Болоньезе", cuisine=ita, ingredients="спагетти, мясной соус, томаты")
Dish.objects.get_or_create(name="Ризотто", cuisine=ita, ingredients="рис арборио, бульон, сыр")
Dish.objects.get_or_create(name="Капрезе", cuisine=ita, ingredients="помидоры, моцарелла, базилик")
Dish.objects.get_or_create(name="Лазанья", cuisine=ita, ingredients="пласты теста, мясной соус, сыр")
Dish.objects.get_or_create(name="Фокачча", cuisine=ita, ingredients="мука, масло, розмарин, соль")
Dish.objects.get_or_create(name="Панна котта", cuisine=ita, ingredients="сливки, желатин, ваниль")
Dish.objects.get_or_create(name="Тирамису", cuisine=ita, ingredients="маскарпоне, кофе, печенье, какао")
Dish.objects.get_or_create(name="Минестроне", cuisine=ita, ingredients="овощи, бульон, фасоль, макароны")
Dish.objects.get_or_create(name="Карбонара", cuisine=ita, ingredients="спагетти, яйца, сыр, бекон")

# Напитки
Drink.objects.get_or_create(name="Чай", category=hot, ingredients="вода, чайные листья")
Drink.objects.get_or_create(name="Кофе", category=hot, ingredients="вода, молотый кофе")
Drink.objects.get_or_create(name="Какао", category=hot, ingredients="молоко, какао-порошок, сахар")
Drink.objects.get_or_create(name="Глинтвейн", category=hot, ingredients="вино, специи, апельсин")
Drink.objects.get_or_create(name="Имбирный чай", category=hot, ingredients="вода, имбирь, лимон, мед")

Drink.objects.get_or_create(name="Лимонад", category=cold, ingredients="вода, лимон, сахар")
Drink.objects.get_or_create(name="Холодный чай", category=cold, ingredients="чай, лимон, лед")
Drink.objects.get_or_create(name="Морс", category=cold, ingredients="вода, ягоды, сахар")
Drink.objects.get_or_create(name="Компот", category=cold, ingredients="вода, фрукты, сахар")
Drink.objects.get_or_create(name="Айс латте", category=cold, ingredients="молоко, кофе, лед")

Drink.objects.get_or_create(name="Эспрессо", category=coffee, ingredients="кофе")
Drink.objects.get_or_create(name="Американо", category=coffee, ingredients="кофе, вода")
Drink.objects.get_or_create(name="Капучино", category=coffee, ingredients="кофе, молоко, пена")
Drink.objects.get_or_create(name="Латте", category=coffee, ingredients="кофе, молоко")
Drink.objects.get_or_create(name="Мокко", category=coffee, ingredients="кофе, молоко, шоколад")

Drink.objects.get_or_create(name="Зеленый чай", category=sugarfree, ingredients="вода, зеленый чай")
Drink.objects.get_or_create(name="Черный кофе", category=sugarfree, ingredients="кофе, вода")
Drink.objects.get_or_create(name="Овощной смузи", category=sugarfree, ingredients="шпинат, огурец, сельдерей")
Drink.objects.get_or_create(name="Травяной настой", category=sugarfree, ingredients="ромашка, вода")
Drink.objects.get_or_create(name="Лимонная вода", category=sugarfree, ingredients="вода, лимон")

