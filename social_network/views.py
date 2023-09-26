from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import ProfilePersonal, ProfilePersonalModel


def feed(request):
    if request.user.is_authenticated:
        user_model_data = User.objects.get(username=request.user.username)
        profile = ProfilePersonal.objects.get(user=user_model_data.pk)
        fields_of_model = ProfilePersonalModel()
        return render(
            request, 'social_network/partials/modal_input_image.html',
            context={
                'user_data': user_model_data,
                'profile_data': profile,
                'fields': fields_of_model
            }
        )


def process_image(request):
    if request.method == 'POST':
        form = ProfilePersonalModel(request.POST, request.FILES)
        username = request.user.username
        if form.is_valid():
            instance_of_profile = ProfilePersonal.objects.get(
                user__username=username
            )
            instance_of_profile.user_image = request.FILES.get(
                'user_image', instance_of_profile.user_image
            )
            instance_of_profile.profile_image = request.FILES.get(
                'profile_image', instance_of_profile.profile_image
            )
            instance_of_profile.save()
            return redirect('feed')
    return redirect('feed')