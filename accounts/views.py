from typing import Any
from django.forms.models import BaseModelForm
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import reverse, reverse_lazy
from .models import RegisterUser, LoginUser
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib.auth.models import User
from utils.create_and_update_form import create_and_update_form
from django.views.decorators.http import require_GET, require_POST
import os
import threading
from social_network.models import ProfilePersonal
import dotenv

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

dotenv.load_dotenv()


class Home(TemplateView):
    template_name = 'account/partials/content-forms_overlay.html'

    def get(self, request, *args, **kwargs):
        request.session.set_expiry(1)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        # save the data of session for populate form of login and register

        context = super().get_context_data(**kwargs)
        context['form'] = create_and_update_form(
            self.request, RegisterUser, 'register_form_data'
        )
        context['login'] = create_and_update_form(
            self.request, RegisterUser, 'login_form_data'
        )
        context['success_message'] = messages.get_messages(self.request)
        return context


# @require_GET
# def home(request):
#     request.session.set_expiry(1)

#     # separando os dados da session de cada formulário
#     form = create_and_update_form(
#         request, RegisterUser, 'register_form_data'
#     )

#     login = create_and_update_form(
#         request, RegisterUser, 'login_form_data'
#     )

#     # Recupera a mensagem de sucesso da sessão
#     success_message = messages.get_messages(request)

#     return render(request, 'account/partials/content-forms_overlay.html', {
#         'form': form,
#         'login': login,
#         'success_message': success_message,
#     })

class CreateUser(CreateView):
    model = User
    template_name = 'account/partials/content-forms_overlay.html'
    fields = ['username', 'email', 'password']
    success_url = 'accounts:account'

    def get_form(self, form_class=None):
        return super().get_form(form_class)

    def form_valid(self, form):
        
        messages.success(
            self.request,
            'account created with success',
            extra_tags='register_form'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(
            self.request, 'something is wrong', extra_tags='register_form'
        )
        return response


# @require_POST
# def create_user(request):
#     POST = request.session['register_form_data'] = request.POST

#     form = create_and_update_form(request, RegisterUser, 'register_form_data')

#     if form.is_valid():
#         user = form.save(commit=False)
#         user.set_password(POST['password'])
#         user.save()

#         user_model_relation = User.objects.get(username=POST['username'])
#         profile = ProfilePersonal(user=user_model_relation)
#         profile.save()

#         del (request.session['register_form_data'])
#         messages.success(
#             request, 'account created with success', extra_tags='register_form'
#         )
#         return redirect('accounts:account')
#     messages.error(
#             request, 'something is wrong', extra_tags='register_form'
#         )
#     return redirect('accounts:account')


@require_POST
def login_user(request):
    POST = request.POST
    request.session['login_form_data'] = POST
    form = LoginUser(POST)
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            del (request.session['login_form_data'])
            return redirect('feed')

    messages.error(request, 'Credentials invalid', extra_tags='login_form')
    return redirect('accounts:account')


def send_email_async(request, username, email):
    user = User.objects.get(username=username)
    uidb64 = urlsafe_base64_encode(force_bytes(user.id))  # type: ignore
    token = default_token_generator.make_token(user)

    root_path = request.build_absolute_uri(
        reverse('password_reset_confirm', args=(uidb64, token))
    )

    send_mail(
            'redefinição de senha',
            f'{root_path}',
            f"{os.environ.get('EMAIL_HOST_USER')}",
            [f"{email}"],
            fail_silently=False,
    )

    return [root_path, str(uidb64), str(token)]


@require_POST
def process_modal_form(request):
    POST = request.POST
    request.session['login_form_data'] = POST
    username, email = [
        request.POST.get('username'), request.POST.get('email')
    ]

    if User.objects.filter(username=username, email=email).exists():

        email_thread = threading.Thread(
            target=send_email_async, args=(request, username, email)
        )
        email_thread.start()
        del (request.session['login_form_data'])
        return JsonResponse({'email': 'Email send'})
    return JsonResponse({'email': 'Something is wrong'})


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('accounts:account')
    template_name = 'account/partials/confirm-reset-password.html'

    def get_context_data(self, **kwargs):
        form = self.get_form()
        form.fields['new_password1'].widget.attrs.update(
            {
                'class': 'input-label-input input',
                'placeholder': 'Password'
            }
        )

        form.fields['new_password2'].widget.attrs.update(
                {
                    'class': 'input-label-input input',
                    'placeholder': 'Confirm Password'
                }
            )

        context = super().get_context_data(**kwargs)
        context['form'] = form
        return context

    def form_valid(self, form):
        # add a success message
        messages.success(
            self.request, "Password change with success!",
            extra_tags='password_change'
        )

        return super().form_valid(form)
