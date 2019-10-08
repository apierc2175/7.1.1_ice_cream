from django.shortcuts import render
from django.http import HttpResponse

from .models import IceCream

# Create your views here.

def index(request):
    # return HttpResponse("Hellow World")
    flavor_list = IceCream.objects.all()

    context = {
        'flavor_list': flavor_list
    }

    return render(request, 'icecream/index.html', context)
