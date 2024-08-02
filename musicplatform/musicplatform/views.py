from django.shortcuts import render

def index(request):
    return render(request, 'mainpage.html')  # Path relative to the templates directory
