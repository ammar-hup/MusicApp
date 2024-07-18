from django.shortcuts          import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth       import authenticate,login,logout
from django.contrib.auth.views import RedirectURLMixin
from django.contrib            import messages
from django.urls               import reverse

class UserLogin(LoginView):
    login_url = '/login/'
    redirect_field_name = 'next'
    template_name = 'registration/login.html'
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        return super().post(request, user)










# def UserLogin(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             messages.success(request,('you have logged in successfully'))
#             return redirect(reverse('login')) 
#         else:
#             # Return an 'invalid login' error message.
#             messages.field(request,('sorry! you dont have an account'))
#             return redirect(reverse('create')) 
#     else:
#         return render(request, 'registration\login.html' ,{})