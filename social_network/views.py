from django.shortcuts import render
from django.contrib.auth.models import User
from .models import ProfilePersonal


def feed(request):
    t = User.objects.get(username='gustavo')
    p = ProfilePersonal.objects.first()
    print(t)
    return render(request, 'social_network/feed.html', context={
        'user_data': t,
        'p': p,
    })
