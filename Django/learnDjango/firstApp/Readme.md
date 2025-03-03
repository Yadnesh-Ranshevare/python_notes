# Creating a New Django App

To create a new Django app, run the following command:

```bash
python manage.py startapp <app_name>
```

This command will generate a new directory structure for your app, which includes the following files and directories:      

```
<app_name>
    ├── migrations
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```
### Explanation of the Generated Files and Directories:
- `migrations/:` 
  This directory contains files that track changes to your models and allow you to apply those changes to the database.
- `__init__.py: `
  This file marks the directory as a Python package.
- `admin.py:` 
  Contains configuration to manage models in the Django admin interface.
- `apps.py: `
  This file defines the app's configuration (metadata such as app name, label, etc.).

- `models.py: `
  Where you define your application's data models.
- `tests.py: `
  This file is for writing tests for your app.
- `views.py:`
   Contains view functions that handle requests and return responses.


### Important Note: 
While Django creates the app folder and its contents, the app is not automatically installed into your main project. To make the main project aware of the new app, you need to add the app to the INSTALLED_APPS list in the settings.py file of your main project.\

For example, add your app name to the list like this:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '<app_name>',  # Add your new app here
]
```
This ensures that Django includes your app when running commands like migrations and during the server startup.

# setting urls.py for our new app

1. create urls.py file into your new app directory with the following settings
```python
from django.urls import path
from . import views

urlpatterns = [
    #you can add your new app path here
]
```

 
2. configure urls.py of main project
```python
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #other paths
    path('firstApp/',include('firstApp.urls'))      # telling django to pass the control to urls.py of the first app directory once user hit the 'firstApp/' route 
]
```

#### Note: URL Routing in Django Apps
When you declare a path in the `urls.py` file of a new app, you don’t need to manually include the app's name (e.g., `firstApp/`) in the route. Django automatically adds the app name to the URL when it's included in the main project’s `urls.py.`

Let me explain this with an example:  
## Example:

In your app's `urls.py` (e.g., `firstApp/urls.py`), you might have the following route:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.firstApp, name="first-app"),     #whenever you hit the '/firstApp/home' route control will pass to views.firstApp 
]
```
This means the path home/ is already prefixed by firstApp/ based on how it's included in the main urls.py, so you don’t have to specify firstApp/ in the app's urls.py.
 