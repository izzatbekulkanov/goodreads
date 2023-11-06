from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookReviewSerializer
from books.models import BookReview


class BookReviewDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        book_review = BookReview.objects.get(id=id)
        serializer = BookReviewSerializer(book_review)
        return Response(data=serializer.data)

    def delete(self, request, id):
        book_review = BookReview.objects.get(id=id)
        book_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        try:
            book_review = BookReview.objects.get(id=id)
        except BookReview.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

        serializer = BookReviewSerializer(instance=book_review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, id):
        book_review = BookReview.objects.get(id=id)
        serializer = BookReviewSerializer(instance=book_review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class BookListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        book_review = BookReview.objects.all()
        serializer = BookReviewSerializer(book_review, many=True)
        return Response(data=serializer.data)


class BookReviewsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        book_reviews = BookReview.objects.all().order_by('-created_at')
        paginator = PageNumberPagination()
        paginator.page_size = 10  # PAGE_SIZE ni to'g'risida
        page_obj = paginator.paginate_queryset(book_reviews, request)

        serializer = BookReviewSerializer(page_obj, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = BookReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
