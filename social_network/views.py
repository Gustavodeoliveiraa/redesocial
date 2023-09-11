from django.shortcuts import render


def t(request):
    return render(request, 'social_network/feed.html')