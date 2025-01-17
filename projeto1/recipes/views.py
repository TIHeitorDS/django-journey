from django.shortcuts import render
from .utils.recipes.factory import make_recipe

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Heitor Claudino',
        'recipes': [make_recipe() for _ in range(10)]
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Heitor Claudino',
        'recipe': make_recipe(),
        'is_detail_page': True
    })
