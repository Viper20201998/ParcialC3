from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass
#admin.site.register(Author)
#admin.site.register(Genre)
#admin.site.register(BookInstance)
