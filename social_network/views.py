from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import ProfilePersonal, ProfilePersonalModel, Status, StatusModel


@login_required
def feed(request):
    user_model_data = User.objects.get(username=request.user.username)
    profile = ProfilePersonal.objects.get(user=user_model_data.pk)
    fields_of_model = ProfilePersonalModel()
    status_fields = StatusModel()
    pp = profile.status_set.all()

    return render(
        request, 'social_network/partials/modal_input_image.html',
        context={
            'user_data': user_model_data,
            'profile_data': profile,
            'fields': fields_of_model,
            'status_fields': status_fields,
            'teste': pp
        }
    )

#change profile image
@login_required
def process_image(request):
    if request.method == 'POST':
        form = ProfilePersonalModel(request.POST, request.FILES)
        username = request.user.username
        if form.is_valid():
            instance_of_profile = ProfilePersonal.objects.get(
                user__username=username
            )
            # delete the old profile image before save the new one
            if instance_of_profile.profile_image:
                instance_of_profile.profile_image.delete(save=True)

            instance_of_profile.profile_image = request.FILES.get(
                'profile_image', instance_of_profile.profile_image
            )

            instance_of_profile.save()
            return redirect('feed')
    return redirect('feed')


def create_status(request):
    if request.method == 'POST':
        form = ProfilePersonalModel(request.POST, request.FILES)
        form_image = form.files.get('status_image')
        user = ProfilePersonal.objects.get(
            user__username=request.user.username
        )
        Status.objects.create(usuario=user, status_image=form_image)
    return redirect('feed')


def logout_view(request):
    logout(request)
    return redirect('accounts:account')
