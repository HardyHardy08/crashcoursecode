"""Defines URL patterns for instabooks"""

from django.conf.urls import url  # url func maps URLs to views

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Show all albums
    url(r'^albums/$', views.albums, name='albums'),

    # Detail page for a single album
    url(r'^albums/(?P<album_id>\d+)/$', views.album, name='album'),

    # Page for adding a new album
    url(r'^new_album/$', views.new_album, name='new_album'),

    # Page for adding a new entry
    url(r'^new_entry/(?P<album_id>\d+)/$', views.new_entry, name='new_entry'),

    # Page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
        name='edit_entry')
]
