from django.shortcuts import render
from listings.choices import price_choices, state_choices, bedroom_choices
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-listing_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('hire_date')[:3]
    for realtor in Realtor.objects.order_by('-id').filter(is_mvp=True)[:1]:
        mvp_realtor = realtor
    context = {
        'realtors': realtors,
        'mvp_realtor': mvp_realtor
    }
    return render(request, 'pages/about.html', context)
