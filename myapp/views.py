from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Food, Consume


@login_required
def index(request):
    if request.method == "POST":
        food_consumed = request.POST.get('food_consumed')
        if food_consumed:
            food_item = get_object_or_404(Food, name=food_consumed)
            Consume.objects.create(user=request.user, food_consumed=food_item)

    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'myapp/index.html', {
        'foods': foods,
        'consumed_food': consumed_food
    })


@login_required
def delete_consume(request, id):
    consumed_food = get_object_or_404(Consume, id=id, user=request.user)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect(reverse('index'))
    return render(request, 'myapp/delete.html', {'consumed_food': consumed_food})