from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('movies', views.movies_view, name="movies"),
    path('movie/<int:movie_id>/', views.movie_detail_view, name="movie_detail"),
    path('movies/<int:movie_id>/comment/',  views.add_comment_view, name="add_comment"),
    path('comment/delete/<int:comment_id>/', views.delete_comment_view, name="delete_comment"),
    path('about/', views.about_view, name="about"),
    path('search/', views.search_view, name="search"),
    path('category/<int:id>/', views.category_detail, name="category_detail"),
]
