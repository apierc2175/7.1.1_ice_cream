from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import IceCream

# Create your views here.

def index(request):
    # return HttpResponse("Hellow World")
    ice_cream_list = IceCream.objects.all()
    ice_cream_list = IceCream.objects.filter(available="WEEKLY")
    # flavor = get_object_or_404(Flavor, pk=flavor_id)

    context = {
        'ice_cream_list': ice_cream_list,
    }

    return render(request, 'icecream/index.html', context)
    # return HttpResponseRedirect(reverse('icecream:index', args=(flavor.id,)))
