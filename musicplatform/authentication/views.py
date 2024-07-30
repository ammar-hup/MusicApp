# authentication/views.py
from django.contrib.auth.views import LoginView
from .forms import SignInForm

class SignInView(LoginView):
    template_name = 'registration/signin.html'
    authentication_form = SignInForm
