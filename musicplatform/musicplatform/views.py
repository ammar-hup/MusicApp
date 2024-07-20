from django.shortcuts import render

def index(request):
    return render(request, 'mainpage/index.html')  # Path relative to the templates directory
