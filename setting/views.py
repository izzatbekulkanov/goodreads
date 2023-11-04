from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from books.models import BookReview


# Create your views here.
def landing_page(request):
    return render(request, "index.html")

def home_page(request):
    book_review = BookReview.objects.all().order_by('-created_at')
    page_size = request.GET.get('page_size', 6)
    paginator = Paginator(book_review, page_size)

    page_num = request.GET.get('page', 1)
    page_object = paginator.get_page(page_num)


    return render(request, 'home.html', {'page_obj': page_object})