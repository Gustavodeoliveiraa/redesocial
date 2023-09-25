from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import ProfilePersonal, ProfilePersonalModel


def feed(request):
    t = User.objects.get(username='gustavo')
    p = ProfilePersonal.objects.first()
    fieldt = ProfilePersonalModel()  # fazer a view q processa imagens
    return render(
        request, 'social_network/partials/modal_input_image.html',
        context={
            'user_data': t,
            'p': p,
            'fieldt': fieldt
        }
    )


def process_image(request):
    if request.method == 'POST':
        form = ProfilePersonalModel(request.POST, request.FILES)
        if form.is_valid():
            data = ProfilePersonal.objects.get(user__username='gustavo')
            data.user_image = request.FILES.get('user_image', data.user_image)
            data.profile_image = request.FILES.get('profile_image', data.profile_image)
            data.save()
            return redirect('feed')
    return redirect('feed')