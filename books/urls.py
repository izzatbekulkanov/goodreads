from django.urls import path
from .views import BooksView, BookDetailView, AddViewView


app_name = 'books'
urlpatterns = [
    path('', BooksView.as_view(), name='list'),
    path('<int:id>/', BookDetailView.as_view(), name='detail'),
    path('<int:id>/reviews/', AddViewView.as_view(), name='reviews'),
]