# app templates
If you have already configured the TEMPLATES setting in the settings.py of your Django project (typically in the root project directory), you do not need to add the templates directory for each individual app manually.

By default, Django will look for templates in a templates/ directory within each app, but the root-level TEMPLATES setting in settings.py defines how templates are handled across the entire project. This configuration includes the directories where Django should look for templates, as well as the template loading mechanism.