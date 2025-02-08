from django.contrib import admin
from .models import Movie,Comment,Category,Contact

admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Contact)