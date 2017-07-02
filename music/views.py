from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# from django.template import loader
from django.conf import settings
from .models import Album, Song

"""                   
#########  Running as a root for accessing superuser data ###############
import os
import sys

euid = os.geteuid()
if euid != 0:
    print "Script not started as root. Running sudo.."
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    # the next line replaces the currently-running process with the sudo
    os.execlpe('sudo', *args)

print 'Running. Your euid is', euid
##########################################################################
"""

# Create your views here.
def  index(request):
	all_albums = Album.objects.all()
	# template = loader.get_template('music/index.html')
	return render(request, 'music/index.html', {'all_albums': all_albums})
	# return HttpResponse(template.render(context, request))

def detail(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'music/detail.html', {'album': album})	
	
def favorite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except (KeyError, Song.DoesNotExist):
		return render(request, 'music/detail.html', {'album': album, 'error_message': "You did not select a valid song",})
	else:
		selected_song.is_favorite = not selected_song.is_favorite
		selected_song.save()
		return render(request, 'music/detail.html', {'album': album})