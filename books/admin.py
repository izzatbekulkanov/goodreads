from django.contrib import admin
from books.models import Book, Author, BookAuthor, BookReview

# Register your models here.

# Book modeli
class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn', 'description',)
    list_display = ('title', 'isbn',)
    # list_filter = ('')

admin.site.register(Book, BookAdmin)


# Author modeli
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'email')
    list_display = ('first_name', 'last_name', 'email', 'bio')

admin.site.register(Author, AuthorAdmin)


#Book review modeli
class BookReviewAdmin(admin.ModelAdmin):
    search_fields = ('user', 'book', 'start_give')
    list_display = ('user', 'book', 'stars_give', 'comment')
    list_filter = ('stars_give',)

admin.site.register(BookReview, BookReviewAdmin)


#BookAuthor Modeli
class BookAuthorAdmin(admin.ModelAdmin):
    search_fields = ('book', 'user')
    list_display = ('author', 'book')

admin.site.register(BookAuthor, BookAuthorAdmin)