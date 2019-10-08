from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import IceCream

# Create your views here.

def index(request):
    ice_cream_list = IceCream.objects.all()

    context = {
        'ice_cream_list': ice_cream_list,
        'heading': 'All'
    }

    return render(request, 'icecream/index.html', context)
    # return HttpResponseRedirect(reverse('icecream:index', args=(flavor.id,)))

def daily(request):
    ice_cream_list = IceCream.objects.filter(available='DAILY')

    context = {
        'ice_cream_list': ice_cream_list,
        'heading': 'Daily Ice Cream Flavors'
    }
    return render(request, 'icecream/index.html', context)

def weekly(request):
    ice_cream_list = IceCream.objects.filter(available='WEEKLY')
    context = {'ice_cream_list': ice_cream_list, 'heading': 'Weekly'}
    return render(request, 'icecream/index.html', context)

def seasonal(request):
    ice_cream_list = IceCream.objects.filter(available='SEASONAL')

    context = {
        'ice_cream_list': ice_cream_list,
        'heading': 'Seasonal Ice Cream Flavors'
    }
    return render(request, 'icecream/index.html', context)
