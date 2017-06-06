from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


from .models import Album, Entry
from .forms import AlbumForm, EntryForm


def index(request):
    """The home page for instabook"""
    return render(request, 'instabooks/index.html')


@login_required
def albums(request):
    """Show all topics"""
    albums = Album.objects.order_by('date_added')
    context = {'albums': albums}
    return render(request, 'instabooks/albums.html', context)


@login_required
def album(request, album_id):
    """Show a single album and all it's entries"""
    album = Album.objects.get(id=album_id)
    entries = album.entry_set.order_by('-date_added')
    # Makes sure the album belongs to the current user.
    if album.owner != request.user:
        raise Http404
    context = {'album': album, 'entries': entries}
    return render(request, 'instabooks/album.html', context)


@login_required
def new_album(request):
    """Add a new album"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = AlbumForm()
    else:
        # POST data submitted; process data
        form = AlbumForm(request.POST)
        if form.is_valid():
            new_album = form.save(commit=False)
            new_album.owner = request.user
            new_album.save()
            return HttpResponseRedirect(reverse('instabooks:albums'))

    context = {'form': form}
    return render(request, 'instabooks/new_album.html', context)


@login_required
def new_entry(request, album_id):
    """Add a new entry in an album"""
    album = Album.objects.get(id=album_id)

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = EntryForm()
    else:
        # POST data submitted; process data
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.album = album
            new_entry.save()
            return HttpResponseRedirect(reverse('instabooks:album',
                                                args=[album_id]))

    context = {'album': album, 'form': form}
    return render(request, 'instabooks/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    album = entry.album
    if album.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data
        form = EntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('instabooks:album',
                                                args=[album.id]))

    context = {'entry': entry, 'album': album, 'form': form}
    return render(request, 'instabooks/edit_entry.html', context)
