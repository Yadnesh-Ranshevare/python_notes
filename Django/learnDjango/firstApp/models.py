from django.db import models  # Importing the models module from Django
from django.utils import timezone  # Importing timezone to set the current time as default

class UserModel(models.Model):
    # A tuple defining the types of users. Choices are either 'normal' or 'admin'.
    USER_TYPES = (('normal', 'Normal User'), ('admin', 'Administrator'))
    
    # The name of the user (max 100 characters).
    name = models.CharField(max_length=100)

    # Image field to store the user's image in a directory called 'user/images/'.
    image = models.ImageField(upload_to='user/images/')

    # The date when the user was added, with the default value being the current time.
    date_added = models.DateTimeField(default=timezone.now)

    # A choice field for the user type. It can be either 'normal' or 'admin'.
    type = models.CharField(max_length=6, choices=USER_TYPES)
    
    def __str__(self):
        return self.name