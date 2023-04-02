from django.urls import path
from . import views

urlpatterns = [
    # path('', views.artist_list, name='artist_list'),
    # path('songs/', views.song_list, name='song_list'),
    # path('artists/<int:pk>', views.artist_detail, name='artist_detail'),
    # path('songs/<int:pk>', views.song_detail, name='song_detail'),
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('songs/', views.SongList.as_view(), name="song_list"),
    path('songs/<int:pk>', views.SongDetail.as_view(), name="song_detail")
]
