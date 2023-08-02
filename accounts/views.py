from django.shortcuts import render, redirect
from .models import RegisterUser, LoginUser
from django.contrib import messages
from django.http import Http404
from django.contrib.auth import login, authenticate

# tela inicial para login ou criação de conta


def entry(request):
    register_form_data = request.session.get('register_form_data', None)
    login_form_data = request.session.get('login_form_data', None)
    # separando os dados da session de cada formulário
    form = RegisterUser(register_form_data)
    login = RegisterUser(login_form_data)

    return render(request, 'account/login_base.html', {
        'form': form,
        'login': login,
    })


def create_user(request):
    if not request.POST:
        Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterUser(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(POST['password'])
        user.save()
        del (request.session['register_form_data'])
        messages.success(
            request, 'account created with success', extra_tags='register_form'
        )
        return redirect('accounts:account')
    else:
        messages.error(
            request, 'something is wrong', extra_tags='register_form'
        )
        return redirect('accounts:account')


def login_user(request):
    if not request.POST:
        Http404()

    POST = request.POST
    request.session['login_form_data'] = POST
    form = LoginUser(POST)
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(
                request, 'Logged with success', extra_tags='login_form'
            )
            del (request.session['login_form_data'])
            return redirect('accounts:account')

    messages.error(request, 'Credentials invalid', extra_tags='login_form')
    return redirect('accounts:account')
