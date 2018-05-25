from django.shortcuts import render

def food_list(request):
    return render(request, 'foodrep/food_list.html', {})
