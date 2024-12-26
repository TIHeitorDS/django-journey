from django.shortcuts import render

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Heitor Claudino Desenvolvedor'
    })

def about(request):
    return render(request, 'recipes/about.html')

def contact(request):
    return render(request, 'recipes/contact.html')
