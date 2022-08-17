from django.shortcuts import render
from cars.models import *


def car_detail(request, pk):
    owner = Driver.objects.get(pk=pk)
    cars = Car.objects.filter(owner_id=owner.id)
    context = {
        "vehicles": cars,
        "drivers": owner,
    }
    return render(request, 'car_detail.html', context)
