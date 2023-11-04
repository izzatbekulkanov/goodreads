from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from books.models import Book
from django.core.paginator import Paginator
from .forms import BookReviewFrom
from .models import BookReview
from django.contrib.auth.mixins import LoginRequiredMixin


class BooksView(View):
    def get(self, request):
        books = Book.objects.all().order_by('id')
        search_query = request.GET.get('q', '')
        if search_query:
            books = books.filter(title__icontains=search_query)


        page_size = request.GET.get('page_size', 3)
        paginator = Paginator(books, page_size)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        return render(
            request,
            'books/list.html',
            {'page_obj': page_obj, 'search_query':search_query})

class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewFrom()

        return render(request, 'books/detail.html', {'book': book, 'review_form':review_form, })


class AddViewView(LoginRequiredMixin ,View):
    def post(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewFrom(data=request.POST)

        if review_form.is_valid():
            BookReview.objects.create(
                book=book,
                user=request.user,
                start_give=review_form.cleaned_data['start_give'],
                comment=review_form.cleaned_data['comment'],
            )

            return redirect(reverse('books:detail', kwargs={'id': book.id}))

        return render(request, 'books/detail.html', {'book': book, 'review_form':review_form, })