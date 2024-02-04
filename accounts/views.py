import os
import threading
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import login, authenticate
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes
from django.views.generic import TemplateView
from django.forms.models import BaseModelForm
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.decorators.http import require_POST
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetConfirmView
from .models import RegisterUser, LoginUser
from utils.create_and_update_form import create_and_update_form


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
            self.request, LoginUser, 'login_form_data'
        )
        context['success_message'] = messages.get_messages(self.request)
        return context


@method_decorator(require_POST, name='dispatch')
class CreateUser(CreateView):
    model = User
    form_class = RegisterUser
    template_name = 'account/partials/content-forms_overlay.html'
    success_url = reverse_lazy('accounts:account')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login"] = LoginUser
        return context

    def form_valid(self, form):
        messages.success(
            self.request,
            'account created with success',
            extra_tags='register_form'
        )
        return super().form_valid(form)

    def form_invalid(self, form: BaseModelForm):
        messages.error(
            self.request, 'something is wrong', extra_tags='register_form'
        )
        return super().form_invalid(form)


@method_decorator(require_POST, name='dispatch')
class UserLogin(FormView):
    template_name = 'account/partials/content-forms_overlay.html'
    form_class = LoginUser
    success_url = reverse_lazy('accounts:account')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            return redirect('feed')

        self.request.session['login_form_data'] = self.request.POST
        messages.error(
            self.request, 'Credentials invalid', extra_tags='login_form'
        )

        return super().form_valid(form)


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
