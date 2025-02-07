from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('movies', views.movies_view, name="movies"),
    path('movie/<int:movie_id>/', views.movie_detail_view, name="movie_detail"),

]
