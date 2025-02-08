from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie, Contact
from . forms import CommentForm

def home_view(request):
    """Renders the "home.html" template and does not send any additional context."""
    return render(request, "home.html")



def movies_view(request):
    movies = Movie.objects.all()
    if request.method == "GET":
        
        return render(request, "movies.html", {"movies": movies})
    


@login_required
def movie_detail_view(request, movie_id):
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
        form = CommentForm()

    context = {
        "movie": movie,
        "comment_form": form,
    }

    return render(request, "movie_details.html", context)




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