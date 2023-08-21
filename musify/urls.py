from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('',views.home,name="home"),
    path('allsongs/', views.allsongs, name="allsongs"),
    path('trending_songs/',views.trending_songs,name="trending_songs"),
    path('arijit/',views.arijit,name="arijit"),
    path('allsongs/<int:id>/', views.songpage, name="songpage"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('likedsong',views.likedsong,name="likedsong"),
    path('logout',views.logout,name="logout"),
    path('search',views.search,name="search"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
