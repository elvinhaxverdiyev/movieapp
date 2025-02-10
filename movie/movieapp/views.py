from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Movie, Contact, Comment
from . forms import CommentForm

def home_view(request):
    """Renders the "home.html" template and does not send any additional context."""
    return render(request, "home.html")



def movies_view(request):
    movie_list = Movie.objects.all()
    paginator = Paginator(movie_list, 4)
    page = request.GET.get("page")
    
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
        
    return render(request, "movies.html", {"movies": movies})



def movie_detail_view(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    comments = Comment.objects.filter(movie=movie).order_by("-created_at")
    form = CommentForm()
    
    contex = {
        "movie": movie,
        "comments": comments,
        "comment_form": form,
    }
    return render(request, "movie_details.html", contex)



@login_required
def add_comment_view(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    
    if request.method == "POST":
        
        form = CommentForm(request.POST)
        
        if form.is_valid():
            
            comment = form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
            return redirect("movie_detail", movie_id=movie_id)
        
        else:
            return render(request, "movie_detail.html", {"movie": movie, "comment_form": form})
        
    return redirect("movie_detail", movie_id=movie_id)



@login_required
def delete_comment_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if comment.user == request.user or request.user.is_superuser:
        movie_id = comment.movie.id
        comment.delete()
        
    return redirect("movie_detail", movie_id=movie_id)



def about_view(request):
    return render(request, "about.html")



def search_view(request):
    query = request.GET.get("q", "").strip()
    if query:
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = Movie.objects.none()
    return render(request, "search.html", {"movies": movies, "search_query": query})




def contact_info(request):
    contact = Contact.objects.all() 
    return render(request, "home.html", {"contact_info": contact})