# templates
In Django, templates are used to define the structure and layout of the HTML pages that are returned as responses to the user. Django's template system allows you to separate the logic of your application (in Python views) from the presentation of data (in HTML).
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

you also need tho mention this templates into the app setting to access in into your app
```python
# inside the settings.py file
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['add_your_template_here'],   #add template directory here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
now you can use your templates wherever you want

#### Nested directory structure
consider your directory structure as 
```
template( folder that mention into setting )/       
    └── child/
         └──index.html/
        
```
in above case declare view as follows
```python
def template(request):
    return render(request,'child/index.html')
```
`note-` settings.py remains the same

## how to load static aset

code for linking static style sheet with templates HTML
```html
<!--  telling template engin that we are loading static aset-->
{% load static %} 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Learn Django</title>
    <link rel="stylesheet" href="{%static 'style.css' %}">  <!-- loading static aset -->
</head>
<body>
    <h1>Learn Django template</h1>
</body>
</html>
```
configuring the settings
```python
import os


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]       #add this with static:- folder containing static aset
```