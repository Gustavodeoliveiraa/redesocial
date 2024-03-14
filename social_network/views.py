from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import ProfilePersonal, ProfilePersonalModel, Notifications
from .models import Status, StatusModel, Post, PostModel
from .models import Friends
from django.http import JsonResponse
from django.templatetags.static import static
from django.db.models import F


@login_required
def feed(request):
    profile = ProfilePersonal.objects.select_related('user')\
        .get(user__username=request.user.username)
    fields_of_model_profile_image = ProfilePersonalModel()
    send_img_post = PostModel()
    status_fields = StatusModel()
    friend_all = Friends.objects.filter(user_reference=profile)\
        .select_related('friend', 'friend__user')\
        .prefetch_related('friend__status_set',)\
        .annotate(friend_name=F('friend__user__username'))

    post = Post.objects.filter(public='public').select_related(
        'user', 'user__user'
        ).annotate(username=F('user__user__username'))\
        .order_by('-id')

    my_status = Status.objects.filter(usuario=profile)\
        .select_related('usuario', 'usuario__user').last()

    my_notifications = Notifications.objects.filter(
        recipient_user=profile, read=False
    )
    notification_count = my_notifications.count()

    print(my_notifications)

    return render(
        request, 'social_network/partials/notify.html',
        context={
            'profile_data': profile,
            'fields': fields_of_model_profile_image,
            'status_fields': status_fields,
            'post_field': send_img_post,
            'friend_all': friend_all,
            'posts': post,
            'my_status': my_status,
            'notification': my_notifications,
            'notify_count': notification_count
        }
    )


#  change profile image
@login_required()
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


@login_required()
def create_status(request):
    if request.method == 'POST':
        form = ProfilePersonalModel(request.POST, request.FILES)
        form_image = form.files.get('status_image')
        user = ProfilePersonal.objects.get(
            user__username=request.user.username
        )
        Status.objects.create(usuario=user, status_image=form_image)
    return redirect('feed')


@login_required()
def show_status_of_a_user(request, user):
    status_of_user = Status.objects.filter(usuario__user__username=user)\
        .select_related('usuario', 'usuario__user')

    status_list = list()

    for status in status_of_user:
        user_status = {
            'user': status.usuario.user.username,
            'profile_image': status.usuario.profile_image.url
            if status.usuario.profile_image else (
                static("img/without_user.png")
            ),
            'status_image': status.status_image.url,
        }

        status_list.append(user_status)
    response_data = {'user_status': status_list}

    return JsonResponse(response_data)


@login_required()
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
            ),
        }

        user_list.append(user_data)
    response_data = {'user': user_list}

    return JsonResponse(response_data)


def send_notify_add_friend(request, user):
    sender = ProfilePersonal.objects.get(user__username=request.user.username)
    recipient = ProfilePersonal.objects.get(user__username=user)

    Notifications.objects.create(
        sender=sender,
        recipient_user=recipient,
        verb=f"{request.user.username} enviou uma solicitação",
    )
    return redirect('feed')


@login_required()
def add_friends(request, user, notify_id):
    Notifications.objects.get(id=notify_id).mark_as_read()
    friend = ProfilePersonal.objects.get(user__username=user)
    reference_user = ProfilePersonal.objects.get(
        user__username=request.user.username
    )

    user_is_a_friend = Friends.objects.filter(
        user_reference=reference_user, friend=friend
    )

    if user_is_a_friend.exists():
        pass
    else:
        Friends.objects.create(
            friend=friend,
            user_reference=reference_user
        )
        Friends.objects.create(
            friend=reference_user,
            user_reference=friend, 
        )
#   TODO: VALIDAR PARA N ENVIAR MAIS DE UMA NOTIFICAÇAO
#   TODO: CRIAR TEMPLATE Q MOSTRA AS NOTIFICAÇOES
    return redirect('feed')


@login_required()
def delete_friend(request, pk):
    try:
        Friends.objects.get(
            pk=pk
        ).delete()
    except Exception as e:
        print('error', e)
    return redirect('feed')


@login_required()
def add_post(request):
    user = ProfilePersonal.objects.get(
        user__username=request.user.username
    )

    form = PostModel(request.POST, request.FILES)
    if form.is_valid():
        new_post = request.POST.get('thinking')
        public_or_private = request.POST.get('post_form_text')

        Post.objects.create(
            user=user,
            text_post=new_post,
            public=public_or_private,
            post_image=request.FILES.get('post_image')
        )

    return redirect('feed')


@login_required()
def num_likes_of_post(reques, post_id, likes):
    try:
        post = Post.objects.get(id=post_id)
        post.likes = likes
        post.save()
    except Post.DoesNotExist:
        pass

    return redirect('feed')


@login_required()
def delete_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        post.post_image.delete()
        post.delete()
    except: # noqa
        pass
    return redirect('feed')


@login_required()
def logout_view(request):
    logout(request)
    return redirect('accounts:account')
