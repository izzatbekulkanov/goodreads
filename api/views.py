from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookReviewSerializer
from books.models import BookReview


class BookReviewDetailAPIView(APIView):
    def get(self, request, id):
        book_review = BookReview.objects.get(id=id)
        serializer = BookReviewSerializer(book_review)
        return Response(data=serializer.data)

