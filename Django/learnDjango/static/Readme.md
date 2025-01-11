# static folder

In Django, the static folder is used to store static files—files that do not change or require any processing by the server during each request. These files are usually resources such as:
- CSS files (for styling the web pages)
- JavaScript files (for client-side interactivity)
- Images (logos, icons, etc.)
- Fonts and other assets

### need to mention this static files into setting.py
```python
import os


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]       #add this with static:- folder containing static aset
```