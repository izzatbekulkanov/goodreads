from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from books.models import Book, BookReview
from users.models import CustomUser


class BookReviewAPITestCase(APITestCase):

    def setUp(self):
        self.db_user = CustomUser.objects.create(username="admin", first_name="Izzatbek")
        self.db_user.set_password("Za0209coder")
        self.db_user.save()

    def test_book_review_detail(self):
        book = Book.objects.create(title="Book1", description="Description1", isbn="1231")
        br = BookReview.objects.create(book=book, user=self.db_user, stars_give=5, comment="Juda yaxshi")

        response = self.client.get(reverse('review-detail', kwargs={'id': br.id}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], br.id)
        self.assertEqual(response.data['stars_give'], 5)
        self.assertEqual(response.data['comment'], "Juda yaxshi")
