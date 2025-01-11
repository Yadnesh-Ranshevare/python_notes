# Django Project Setup Guide

This guide will walk you through the process of setting up a Django project using a virtual environment, along with instructions for running your project and understanding the project structure.

## Prerequisites

Make sure you have Python installed on your machine. You can download the latest version of Python from the official website: [Python Download](https://www.python.org/downloads/).

# Installation

### 1. Install `uv` (Ultra-fast Package Manager)

`uv` is a package manager that is faster than `pip` and can be used to install and manage dependencies in your Django project.

To install `uv`, use the following command:

```bash
pip install uv
```
this step is optional and if you skip it just remove the `uv` prefix for `pip` install commands.




### 2. Set Up a Virtual Environment

A virtual environment allows you to isolate your project's dependencies, preventing conflicts with other projects.

#### Create the Virtual Environment

Run the following command to create a virtual environment named :

```bash
py -m venv <-environment name-> #this is a normal method for creating virtual environment
```
we can also create a virtual environment by using `uv` package manager which is much faster than `pip`

```bash
uv .vene    #this will create a virtual environment folder named .venv
```
### 3. Activating virtual environment
To activate the virtual environment, use the following command:
```bash
.venv\Scripts\activate
```
After activation, your terminal prompt should change to indicate that the virtual environment is active.


### 4. create Django project
1. Use `uv` for Package Management: From now on, use `uv` as a prefix to the `pip` install commands to install Django packages
```bash
uv pip install django  #this will install Django dependencies
```

2. Run the following command to create a new Django project
```bash
django-admin startproject <project_name>
```


### 5. Run the Django application
1. Navigate to Your Project Folder: Go into the directory where your Django project was created:
```bash
cd <project_name>
```
2. Run the Development Server: Start the Django development server with the following command:
```bash
python manage.py runserver
```
it will also create the db.sqlite3 file which is default database use in django

---

# File Structure 

#### After creating your Django project, you will see a folder structure like this:
```bash
project_name/
    ├── manage.py
    └── project_name/
        ├── __pycache__/
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

###  Key Files in the Project
- #### manage.py:
  This is the `entry point` to manage the Django project. You will use it to run server commands and interact with the project.

- #### `__pycache__:`
  This folder is automatically created by Python to store compiled bytecode files for optimization and caching.

- #### `__init__.py:`
  This file indicates that the directory should be treated as a Python package.

- #### asgi.py:
  This is the entry point for ASGI-compatible web servers, used for handling asynchronous tasks.

- #### settings.py:
   The configuration file where you set up settings for your Django project, including database configuration, installed apps, middleware, etc.

- #### urls.py:
  This file is responsible for routing incoming requests to the appropriate views (functions or classes that handle the request).

- #### wsgi.py:
  This is the entry point for WSGI-compatible web servers, used for synchronous communication.

---
  # Flow of a Django Application

The flow of a typical Django application can be understood step-by-step as follows:

1. **User Sends a Request to the Server**
   - The flow begins when a user sends an HTTP request (e.g., visiting a URL in their browser) to the server.

2. **Request Accepted by Django**
   - The request is received by the Django server. Django, which is built on the WSGI or ASGI interface, handles incoming requests.

3. **URL Resolver Resolves the Request**
   - Django uses a URL resolver to determine which view should handle the incoming request. 
   - The URL resolver checks the request's URL against the patterns defined in the `urls.py` file of the project and the respective app.
   - It redirects the request to the appropriate **view function** or **view class**.

4. **View (Controller) Handles the Request**
   - The corresponding **view** (located in `views.py`) is invoked to process the request.
   - The view acts as the **controller** that contains the logic to handle the request.
   - The view may interact with the **database** (via models) to fetch or manipulate data.

5. **Sending the Response**
   - Once the view processes the request, it prepares a **response**.
   - The response can either be a simple **HTTP response** (like text or JSON) or an HTML page rendered via a **template** (using Django's templating engine).
   
6. **Return Response to the User**
   - Finally, the response is sent back to the server, which sends it to the user's browser or client, completing the request-response cycle.
   - If the response is HTML, it might include data dynamically generated by the server, populated through templates.

---

# Django Project Structure

## 1. Project Level
The project level is the highest level in the structure and represents the entire Django application. When you start a new Django project using the `django-admin startproject` command, it creates a directory containing settings and configuration files that define the global configuration for your application.

### Key Files at Project Level:
- **`manage.py`**: The command-line utility that allows you to interact with the Django project (runserver, migrate, create apps, etc.).
- **`settings.py`**: The configuration file for the project, where you define settings like database configurations, middleware, installed apps, static files, etc.
- **`urls.py`**: Contains the URL routing for the project. This is where you define URL patterns for different views or apps in the project.
- **`wsgi.py`**: WSGI configuration for deploying the application to a web server (used in production).
- **`asgi.py`**: ASGI configuration for handling asynchronous requests, useful for handling WebSockets and other async tasks.

## 2. App Level
A Django project is typically made up of multiple apps. An app is a self-contained module that performs a specific functionality (e.g., a blog, user authentication, or product catalog). Each app has its own set of files responsible for handling its logic and features.

### Key Files at App Level:
- **`models.py`**: Defines the data models of the app, i.e., the database structure, fields, relationships, etc.
- **`views.py`**: Contains the logic for handling requests and returning responses (usually HTML, JSON, or other types of responses).
- **`urls.py`**: URL configuration specific to this app, where you define routing for views within the app.
- **`admin.py`**: Contains configurations for integrating the app’s models with Django's admin interface.
- **`apps.py`**: Configurations for the app itself (like the app's name).
- **`migrations/`**: Folder containing migration files that track changes to models and allow for applying them to the database.
- **`tests.py`**: Contains unit tests for the app.

## 3. Model Level
Within each app, models represent the database structure and define how data is stored. Models are Python classes that subclass `django.db.models.Model`. Each model defines the fields and behaviors of the data you want to store.

### Key Points:
- **Database schema**: Models are responsible for creating tables in the database.
- **Relationships**: You define relationships like one-to-many, many-to-one, and many-to-many between models.

## 4. View Level
At the view level, Django handles the business logic that processes requests and returns responses. Views take in HTTP requests, interact with models or other data sources, and return HTTP responses (e.g., HTML, JSON).

### Key View Types:
- **Function-based views (FBVs)**: Simple Python functions that take requests and return responses.
- **Class-based views (CBVs)**: More complex views written as Python classes that provide better reusability and extendability.

Views are responsible for interacting with templates, models, and serializers (for APIs).

## 5. Template Level
Django uses templates to define the HTML structure of the web pages. Templates are responsible for rendering dynamic data (from models or views) into HTML, which is sent to the user's browser.

### Key Points:
- Templates are usually stored in the `templates/` directory.
- You can use Django’s template language to embed Python-like logic (loops, conditionals) into HTML.

## 6. Static Level
Static files are non-dynamic files that don’t change with the request. These include images, CSS files, JavaScript files, and fonts.

### Key Points:
- Static files are typically stored in a `static/` directory in your project or app.
- In production, static files are often served by a web server like Nginx or Apache, not Django itself.

## 7. Database Level
The database level represents where the data is stored for your Django project. Django uses models to map to database tables.

### Key Points:
- Django supports various databases like **SQLite** (default), **PostgreSQL**, **MySQL**, **Oracle**, etc.
- The migrations system helps in applying database changes when models are modified.

## 8. Middleware Level
Middleware is a framework of hooks into Django’s request/response processing. It is a layer that sits between the request and the view, processing requests before they reach the view and responses before they are sent to the client.

### Common Middleware Tasks:
- **Request processing** (authentication, logging, etc.)
- **Response processing** (caching, header manipulation, etc.)

You can configure middleware in the `settings.py` file under the `MIDDLEWARE` setting.

## 9. Admin Level
The admin interface provides a web-based interface to manage and interact with the data in your database. It is automatically generated based on your models.

### Key Points:
- You configure the admin interface in `admin.py` of each app.
- Admin is useful for quickly adding, editing, or deleting data without needing to manually interact with the database.

## 10. Testing Level
Django has a built-in testing framework for writing and running tests. It is important to test your application to ensure it works as expected.

### Key Points:
- The test code is typically placed in the `tests.py` file of an app.
- Django’s test framework is built on top of Python’s standard `unittest` module, and you can write test cases for models, views, forms, etc.

---

