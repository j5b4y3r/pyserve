from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('home/', views.home, name='homepage'),
    path('<path:path>', views.send_ff, name='ff'),
    path('home/<path:path>', views.send_ff, name='ff'),
    path('download/<path:file_path>', views.download_file, name='download_file'),
    path('play/<path:file_path>', views.play_file, name='play_file'),
]
