# Poetry Commands

Here are some useful commands and tips for working with poetry.

To initialize poetry :
```
poetry init
```
To enter the poetry virtual environment (venv) :
```
poetry shell
```
To Add packaged to poetry (django for example) :
```
poetry add django
```
To exit the poetry venv :
```
exit
```

# Django Commands

Here are some useful commands and tips for working with Django.

To check the installed Django version:

```
py -m django --version
```

To create a new Django project:

```
django-admin startproject mysite
```

To create a superuser for the admin site:

```
py manage.py create superuser
```
To start the server:

```
py manage.py runserver
```

To create a new app:

```
py manage.py startapp polls
```
## Models and Database and Views

To work with models (database):

1. Make a new app which you will use this data in it. Connect it to your main app by using the `settings.py` file 
3. Make a new file in your new app called `urls.py` and connect it with the main app `urls.py` by the `include` method :
    1. myapp -> urls.py 
    ```
    from django.urls import path

    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```
    2. mysite -> urls.py
    ```
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path('myapp/', include('myapp.urls')),
        path('admin/', admin.site.urls),
    ]
    ```
4. make the view go to `views.py` in ur app :
```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the myapp index.")
```
4. Go to your `models.py` file then start to specify the data into a class
5. We will use the `models` which is imported by Django and it has all fields we need
6. The code will be something like this:

```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50,verbose_name'Title',default = 'Name')    # the product name
    content = models.TextField(null = True, blank = True)              # the product content
    price = models.DecimalField(max_digits=6,decimal_places=2)    # product price
    image = models.ImageField(upload_to='photos/%y/%m/%d')        # product image
    active = models.BooleanField(default=True)               # product status (active / not active)
    socialLink = models.URLField(null=False)                # social link validetor
    creation_datetime = models.DateTimeField(auto_now_add=True) # date and time 
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE) # one to many relationship 

    class Meta :
        verbose_name = "Product"  # the name in admin page
        # ordering = ['name']     # order the products by name
        ordering = ['price']      # order the products by price
```
7. Go to the settings file and add your new app to the INSTALLED_APPS list.
8. To add the Product class to the database, run the following commands:
8. `py manage.py makemigrations` to create a new migration file.
8. `py manage.py migrate` to apply the migration and create the table in the database.
9. Now, you can add, edit, or remove a product from the admin page. To access the admin page, go to `localhost:8000/admin/` in your browser.
10. to show the items in the admin panal to edit them go to `admin.py` file in ur app :
```
from .models import appClassName

admin.site.register(appClassName)
```
11. For the image part, we will split the pics into folders named (year, month, day), and that will be helpful and increase our website speed. We will use (`upload_to='folder name </photo> /%y/%m/%d'`).

## Templates

To create a new template:

1. First, create a folder named 'templates' and make a folder with the page name in it
2. Then, make an `index.html` file in it 
3. Go to the main project settings file and import the os library (`import os`)
4. Go to `DIRS` section and add the HTML templates folder path to it (`os.path.join(BASE_DIR,'templates')`)
5. Go to the views file in the page and use a function to return the template:

```
def index(request):
    return render(request,'mainpage/index.html')
```

To make a base template file and inherit it in other HTML files:

1. Make a `base.html` file in templates folder
2. Write your HTML and CSS in it 
3. Go to the `index.html` file
4. Extend the `base.html` file to use it in your file by writing: `{% extends 'file path' %}` 
5. In our case, it will be like that: `{% extends 'base.html' %}`
6. To write HTML code in the file that has the extend line (`{% extends 'base.html' %}`), you need to use the block element 
7. The block element has an opening and closing tag, like this:

```
{% block (block name) %}
	content
{% endblock %}
```

8. Then, you should go to the `base.html` (the parent file) and add the two blocks (start and end):

```
{% block content %}
{% endblock content %}
```

If you want to make a footer or a navbar and use it in all pages of your project:

1. Make a folder for all the parts in your project (head, body, footer)
2. Make a `footer.html` file in the `parts` folder
3. Go to the `base.html` file and use the include line (like the block element before): `{% include 'file path' %}` the file that we make in parts folder
4. In this case, it will be like this: `{% include 'parts\footer.html' %}`

## HTML and Blocks

To use `if`, `elif`, `else`, `for` with HTML by blocks:

```
{% if name == 'ammar' %}
	<h1> hi <h1>
{% elif name == 'ammar' %}
	<h1> no <h1>
{% else %}
	<h1> not found <h1>
{% endif %}

{% for x in name %}
	<p>{{x}}<p>
{% endfor %}
```

## Static Files

To add images, CSS, and JS files to your project by static files:

1. Make a folder named 'static' in your project

2. Make a folder for each file you will add to your project (CSS, JS, images)

3. Add the file to its folder 

4. Go to `settings.py` file in the project to activate the static files

5. Go to the `STATIC_URL` section and add the static folder path that you have created

6. Write these lines : 
    ```
    STATIC_ROOT = os.path.join(BASE_DIR,'static')
    STATIC_URL = 'static/'
    STATICFILES_DIR = [ os.path.join(BASE_DIR,'project/static') ]
    ```

7. Run the command `py manage.py collectstatic`
8. That will create a new static folder in your hierarchy beside the project, and it will have a folder named `admin`

To enable these files to your HTML:

1. Go to your HTML file (`base.html` for example) and write these two lines:

```
{% load static %}
```

2. Then, add the file that you want (image/CSS/JS) by its tag in HTML (for example, here we add CSS file):

```
<link rel="stylesheet" href="{% static 'css\style.css' %}">
```

If you want to add an image, you should first put the image in the `static/images` folder in the project, then use:

```
{% load static %}
{% block content %}
<img src="{% static 'image/male.png' %}" alt="not found!">
{% endblock content %}
```


## Admin Panel

To make an administration account and manage your products:

1. Run `py manage.py createsuperuser`
2. Then, choose a name, email, and password
3. Run the server and go to `/admin`
4. to view the products name on cards you can use :
```
def __str__(self):
        return self.name    
```
5. to change anything in the `products` group you can use the Meta class:
    ```
    class Meta :
            verbose_name = "Product"  # the name in admin page
            # ordering = ['name']     # order the products by name
            ordering = ['price']      # order the products by price
    ```
    or u can order them by another way :
    ```
    Product.objects.all().order_by('price')
    ```

6. to make a category feild we should make a list of tupels with 2 values with the same name 1 for the system and the other for the database :
    ```
    l = [
            ('mobile','mobile'),
            ('laptop','laptop'),
            ('accessories','accessories'),
            ('headphones','headphones'),
            ('camera','camera'),
        ]
        category = models.CharField(max_length=50, null=True, blank=True, choices=l)

    ```

7. to get the number of products :

    ```
    return render(request,'products/products.html',{'productsName': str(Product.objects.all().count())})
    ```

    8. to make exclude for objects :
    ```
    Product.objects.all().exclude(price = 100)
    ```

9. to get the object that contains chars or numbers :
    ```
    Product.objects.all().filter(name__contains = 'a')
    ```
    or
    ```
    Product.objects.all().filter(price__in =[10,100] )
    ```
    or
    ```
    Product.objects.all().filter(price__range =(10,100))
    ```
## Displaying Products in a Website

To display the products you added on a web page:

1. Go to the templates folder and make a new folder named 'products'.
2. Make two HTML files: product.html and products.html .
3. Go to the views file in the product folder and make two methods (product, products):

    ```
    from django.shortcuts import render
    from .models import Product

    def product(request):
        return render(request, 'products/product.html')

    def products(request):
        return render(request, 'products/products.html', {'productsName': Product.objects.all()})
    ```
4. Go to the products.html file and make a block content for the code and make a for loop on the products to view it:
    ```
    {% block content %}
        {% for x in productsName %}
            <h1>{{x.name}}</h1>
            <h5>{{x.content}}</h5>
            <span>{{x.price}} $</span>
        {% endfor %}
    {% endblock content %}

    ```
5. To add the URL for the products page, go to the `urls.py` file in the product folder and add the new URL:
    ```
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.products, name='products'),
        path('<int:product_id>/', views.product, name='product'),
    ]

    ```
5.  Now, you can access the products page by going to `localhost:8000/products/` in your browser.

6. to get only one object use : 
    ```
    Product.objects.get(name = 'realme')
    ```

7. to add filter for the objects use :
    ```
    Product.objects.all().filter(price = 50)
    ```
    In this case it will show all items with price equal to 50
    

## Activate Media 

to active the media (images,videos) in the project

1. we go to the `settings.py` file in the project folder and go to the bottom after the `Static` section

2. Write these lines : 
    ```
    MEDIA_ROOT = os.path.join(BASE_DIR,'media')
    MEDIA_URL = '/media/'
    ```

3. we will go to the `urls.py` file in the project folder and import those :
    `from django.conf import settings`
    `from django.conf.urls.static import static`

4. we will call `(MEDIA_ROOT , MEDIA_URL)` after we imported the static :
    ```
    urlpatterns = ["the content in it"] + 
    static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)   
    ```
5. now to make the image show up in the website by writing this to the html page:
    `<img src="{{x.image.url}}" alt="">`

## Form With Django
how to make a form in django anf recive the data and store it in the database
we have many ways to do this with django 

#### the first method

1. we add the form in the templates for example `about.html` page cuz its empty : 
    ```
    {% block content %}

    <form action="" method="POST">
        {% csrf_token %}
        <br>
        <input type="text" name="username" placeholder="username">
        <br>
        <input type="password" name="password" placeholder="password">
        <br>    
        <input type="submit" value="save" >

    </form>

    {% endblock content %}
    ```

2. go to the `models.py` file and create new class for the form :
    ```
    class Login(models.Model):
        username = models.CharField(max_length=20)
        password = models.CharField(max_length=20, blank=False)
    ```
    and we need to import this `Login` class to the `views.py` so i can use it :
    `from . models import Login`

3. we go to `views.py` file to take the comming data and put it in models :
   go to the function that controls the page we made the form in , in this case `about` and the parameter `request ` that we passed to the function it will have the data :

   ```
   def about(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    data = Login(username = username, password = password) # to store the data
    data.save() # to save the data from the Login page
    return render(request,'mainpage/about.html')

   ```
4. the we go to the `admin.py` file to save the models :
    ```
    from .models import Login

    admin.site.register(Login)
    ```
    now the data will be in the `Logins` table in the adminstration database
    

#### the second method

we will use a django liberary for the form

1. make a file in the page folder named `forms.py` 

2. go to `forms.py` and write :
    ```
    from django import forms

    class Login(forms.Form):
        username = forms.CharField(max_length=20)
        password = forms.CharField(max_length=30)
    ```
    we have some attributes that we can use in the form
    ```
    # lable
    # initial
    # disabled
    # help_text
    # widget
    # required
    # for example : 
    password = forms.CharField(max_length=30, label = 'pass', required = True, widget = forms.PasswordInput)


    ```
3. then go to `views.py` file to view the content it the website by the context method
    ```
    from . forms import LoginForm

    def about(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    data = Login(username = username, password = password)
    data.save()
    return render(request,'mainpage/about.html' , {'LF' : LoginForm})
    ```
4. then go to the templates folder to the `about.html` file and write : 
    ```
    <form action="" method="POST">
        {% csrf_token %}
        {{LF}}
        <input type="submit" value="save" >
    </form>
    ```
#### the third method #####(the best way)
we will use the data from `models` to make the form (it's like a combination between method 1 and 2)

1. make a file in the page folder named `forms.py` 

1. go to `forms.py` and call the models :
    ```
    from .models import Login

    class LoginForm(forms.ModelForm):
        class Meta:
            model = Login
            fields = '__all__'
            # or : fields = ['username']
    ``` 
2. the `models.py` will stay as it is :
    ```
    from django.db import models

    class Login(models.Model):
        username = models.CharField(max_length=20)
        password = models.CharField(max_length=20, blank=False)
    ```
3. the `views.py` will be like this :
    ```
    def about(request):
        dataform = LoginForm(request.POST)
        dataform.save()
        return render(request,'mainpage/about.html' , {'LF' : LoginForm})
    ```
