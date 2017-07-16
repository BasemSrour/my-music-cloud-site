from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.generic import View
from .models import Album, Song
from .forms import UserForm


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


def favorite_album(request, album_id):
    try:
        album = get_object_or_404(Album, pk=album_id)
        album.is_favorite = not album.is_favorite
        album.save()
    except (KeyError, Album.DoesNotExist):
        return JsonResponse({'success': False})

    return JsonResponse({'success': True})


class SongDetailView(generic.DetailView):
    model = Song
    template_name = 'music/song-details.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({'album': self.get_object().album})
        return context


class SongCreate(CreateView):
        model = Song
        fields = ['file_type', 'song_title']


class SongUpdate(UpdateView):
        model = Song
        fields = ['file_type', 'song_title']


class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('music:index')


def favorite_song(request, song_id):
    try:
        song = get_object_or_404(Song, pk=song_id)
        song.is_favorite = not song.is_favorite
        song.save()
    except (KeyError, Song.DoesNotExist):
        return JsonResponse({'success': False})

    return JsonResponse({'success': True})


class UserForm(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})
