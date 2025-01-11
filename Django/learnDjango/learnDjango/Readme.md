# Views and url mapping

#### view
view is a function or class that receives a web request and returns a web response. The response can contain HTML content, redirections, images, JSON data, or any other form of content.
```python
from django.http import  HttpResponse

def home(request):
    return HttpResponse("Hello, World! This is my first Django app.")
```

you can also return a html response, to do that you need to first create a template which will get rendered on request
- the template
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Learn Django</title>
</head>
<body>
    <h1>Learn Django template</h1>
</body>
</html>
```

- the view
```python
def template(request):
    return render(request, 'template_path')
```

#### url mapping
URL mapping in Django refers to the process of linking a specific URL (Uniform Resource Locator) pattern to a corresponding view function or class
example considering above view
```python
#inside the urls.py file 
from django.contrib import admin
from django.urls import path
from . import views     #import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),       #add this path
    path('templates/', views.template)      #add this path
]
```