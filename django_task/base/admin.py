from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Favourites)
admin.site.register(Genre)
admin.site.register(Author)