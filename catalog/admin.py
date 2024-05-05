from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
    list_display = ('title',
                    'author',
                    'display_genre')
class BooksInline(admin.TabularInline):
    model = Book
@admin.register(Author)
# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    inlines = [BooksInline]
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

admin.site.register(Genre)


# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display =('id','status','book','borrower','due_back','imprint')
    fieldsets = (
            (None, {
                'fields': ('book', 'imprint', 'id')
            }),
            ('Availability', {
                'fields': ('status', 'due_back','borrower')
            }),
    )


admin.site.register(Language)
