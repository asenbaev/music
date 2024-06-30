
from django.urls import path
from . import views
from django.urls import path
from .views import MusicFileListCreate, MusicFileDetail, music_list, music_detail

urlpatterns = [
    path('', views.index, name='index'),
    path('api/music/', MusicFileListCreate.as_view(), name='music-list-create'),
    path('api/music/<int:pk>/', MusicFileDetail.as_view(), name='music-detail'),
    path('music/', music_list, name='music-list'),
    path('music/<int:pk>/', music_detail, name='music-detail-view'),

]




