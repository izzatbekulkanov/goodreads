from django import forms

from books.models import BookReview


class BookReviewFrom(forms.ModelForm):
    start_give = forms.IntegerField(min_value=1, max_value=5,)
    class Meta:
        model = BookReview
        fields = ('start_give', 'comment',)