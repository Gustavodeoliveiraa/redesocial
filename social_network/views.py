from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import ProfilePersonal, ProfilePersonalModel, Status, StatusModel, Post
from .models import Friends
from django.http import JsonResponse
from django.templatetags.static import static
from django.db.models import F


def feed(request):
    profile = ProfilePersonal.objects.select_related('user')\
        .get(user__username=request.user.username)
    fields_of_model = ProfilePersonalModel()
    status_fields = StatusModel()
    friend_all = Friends.objects.filter(user_reference=profile)\
        .select_related('friend',)\
        .prefetch_related('friend__status_set',)\
        .annotate(friend_name=F('friend__user__username'))

    post = Post.objects.filter(public='public').select_related('user')\
        .annotate(username=F('user__user__username'))\
        .order_by('-id')

    return render(
        request, 'social_network/partials/feed.html',
        context={
            'profile_data': profile,
            'fields': fields_of_model,
            'status_fields': status_fields,
            'friend_all': friend_all,
            'posts': post
        }
    )


#  change profile image
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
    new_user = ProfilePersonal.objects.filter(user__username__icontains=user)\
        .exclude(user__username=request.user.username)
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


def add_friends(request, user):
    friend = ProfilePersonal.objects.get(user__username=user)
    reference_user = ProfilePersonal.objects.get(
        user__username=request.user.username
    )
    Friends.objects.create(
        friend=friend,
        user_reference=reference_user
    )
    return redirect('feed')


def add_post(request):
    user = ProfilePersonal.objects.get(
        user__username=request.user.username
    )

    new_post = request.POST.get('thinking')
    public_or_private = request.POST.get('post_form_text')
    Post.objects.create(
        user=user,
        text_post=new_post,
        public=public_or_private
    )
    return redirect('feed')


def logout_view(request):
    logout(request)
    return redirect('accounts:account')
