from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from .models import Dish, Drink
import json,random

def homepage(request):
    return render(request, 'webapp/index.html')

def random_combo(request):
    try:
        dishes = list(Dish.objects.all())
        drinks = list(Drink.objects.all())

        if not dishes or not drinks:
            return JsonResponse({'error': 'Нет блюд или напитков в базе'}, status=400)

        dish = random.choice(dishes)
        drink = random.choice(drinks)

        return JsonResponse({
            'dish': {
                'name': dish.name,
                'cuisine': dish.cuisine.name,
                'ingredients': dish.ingredients
            },
            'drink': {
                'name': drink.name,
                'category': drink.category.name,
                'ingredients': drink.ingredients
            }
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
 
@csrf_exempt
def random_combo_filtered(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Получаем фильтры из запроса
            excluded_cuisines = [x.strip() for x in data.get('exclude_cuisines', [])]
            excluded_ingredients = [x.strip().lower() for x in data.get('exclude_ingredients', [])]
            excluded_drink_categories = [x.strip() for x in data.get('exclude_drink_categories', [])]


            # Фильтрация блюд
            dishes = Dish.objects.all()

            # Исключаем кухни
            excluded_cuisines = [x.strip() for x in data.get('exclude_cuisines', [])]

            if excluded_cuisines:
                dishes = dishes.exclude(cuisine__name__in=excluded_cuisines)


            # Исключаем по ингредиентам
            for ingredient in excluded_ingredients:
                dishes = dishes.exclude(ingredients__icontains=ingredient)

            # Фильтрация напитков
            drinks = Drink.objects.all()

            # Исключаем категории напитков
            for category in excluded_drink_categories:
                drinks = drinks.exclude(category__name__iexact=category)

            # Проверка наличия записей
            if not dishes.exists():
                return JsonResponse({'error': 'Нет подходящих блюд'}, status=400)
            if not drinks.exists():
                return JsonResponse({'error': 'Нет подходящих напитков'}, status=400)

            for d in dishes:
                print(f"- {d.name} ({d.cuisine.name})")

            
            # Случайный выбор
            dish = random.choice(list(dishes))
            drink = random.choice(list(drinks))

            return JsonResponse({
                'dish': {
                    'name': dish.name,
                    'cuisine': dish.cuisine.name,
                    'ingredients': dish.ingredients
                },
                'drink': {
                    'name': drink.name,
                    'category': drink.category.name,
                    'ingredients': drink.ingredients
                }
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Только POST'}, status=405)