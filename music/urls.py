from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
	# /music/
	url(r'^$', views.IndexView.as_view(), name='index'),
	# /music/<album.id>/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	# /music/album/add/
	url(r'^album/add/$', views.AlbumCreate.as_view(), name='add-album'),
	# /music/album/<album.id>/
	url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='update-album'),
	# /music/album/<album.id>/delete/
	url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='delete-album'),
	# /music/song/<song.id>/details/
	url(r'^song/(?P<pk>[0-9]+)/details/$', views.SongDetailView.as_view(), name='song-details'),
	# /music/song/add/
	url(r'^song/add/$', views.SongCreate.as_view(), name='add-song'),
	# /music/song/<song.id>/
	url(r'^song/(?P<pk>[0-9]+)/$', views.SongUpdate.as_view(), name='update-song'),
	# /music/song/<song.id>/delete/
	url(r'^(?P<pk>[0-9]+)/song/delete/$', views.SongDelete.as_view(), name='delete-song'),
]
