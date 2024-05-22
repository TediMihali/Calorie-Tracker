from django.shortcuts import redirect, render
from .models import Food, Consume
# Create your views here.

def index(request):

    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consumed = Food.objects.get(name=food_consumed)
        user = request.user
        consumed_food = Consume(user = user, food_consumed = consumed)
        consumed_food.save()

    consumed_food = Consume.objects.filter(user=request.user)
    foods = Food.objects.all()
    return render(request, "myapp/index.html", {"foods":foods, "consumed_foods": consumed_food})

def delete_consume(request, id):
    item = Consume.objects.get(id=id)

    if request.method == "POST":
        item.delete()
        return redirect('/')
    
    return render(request, 'myapp/delete.html')