from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import ProfilePersonal, ProfilePersonalModel, Status, StatusModel
from .models import Friends
from django.http import JsonResponse
from django.templatetags.static import static


def feed(request):
    profile = ProfilePersonal.objects.select_related('user')\
        .get(user__username=request.user.username)
    fields_of_model = ProfilePersonalModel()
    status_fields = StatusModel()
    friend_all = Friends.objects.filter(user_reference=profile)\
        .select_related('friend', 'user_reference')

    return render(
        request, 'social_network/partials/modal_input_image.html',
        context={
            'profile_data': profile,
            'fields': fields_of_model,
            'status_fields': status_fields,
            'friend_all': friend_all,
        }
    )


#change profile image
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


def show_status_of_a_user(request, user):
    return redirect('feed')


def search_users(request, user):
    new_user = ProfilePersonal.objects.filter(user__username__icontains=user)
    user_list = []

    for people in new_user:
        user_data = {
            'username': people.user.username,
            'email': people.user.email,
            'image': request.build_absolute_uri(people.profile_image.url)
            if people.profile_image else (
                static("img/without_user.png")
            )

            
        }
        user_list.append(user_data)
    response_data = {'user': user_list}

    return JsonResponse(response_data)


def logout_view(request):
    logout(request)
    return redirect('accounts:account')
