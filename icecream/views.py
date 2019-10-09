from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

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

def likes(request, pk):
    # show_like = ice_cream.likes.get(pk=request.POST['ice_cream'])
    # show_like.likes = show_like.likes + 1
    # show_like.likes.save()
    ice_cream = get_object_or_404(IceCream, pk=pk)
    ice_cream.likes += 1
    ice_cream.save()

    return HttpResponseRedirect(reverse('icecream:index'))
