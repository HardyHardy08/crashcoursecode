from django.contrib import admin

# Register your models here.

from instabooks.models import Album, Entry

admin.site.register(Album)
admin.site.register(Entry)
