from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Album(models.Model):
    """A album the user will post pictures of"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text


class Entry(models.Model):
    """Entry into a album consisting of a picture and a description"""
    album = models.ForeignKey(Album)
    image = models.FileField(upload_to='pic_folder/',
                             default='pic_folder/None/no-img.jpg')
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        return self.text[:50] + "..."
