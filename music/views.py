from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# from django.shortcuts import get_object_or_404
# from django.http import JsonResponse
from .models import Album, Song


class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_albums'

	def get_queryset(self):
		return Album.objects.all()


class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'


class AlbumCreate(CreateView):
		model = Album
		fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
		model = Album
		fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')


class SongDetailView(generic.DetailView):
	model = Song
	template_name = 'music/song-details.html'


class SongCreate(CreateView):
		model = Song
		fields = ['file_type', 'song_title']


class SongUpdate(UpdateView):
		model = Song
		fields = ['file_type', 'song_title']


class SongDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:detail')
