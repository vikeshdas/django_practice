from django.db import models
from django.contrib.auth.models import User #this is the User that we find at the /admin page

# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True) # It is not required
    # pip install pillow to use this!

    # The profile_pics has to be an fodler inside of the media directory we added last time
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
