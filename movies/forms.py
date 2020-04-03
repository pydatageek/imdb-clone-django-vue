from django import forms

from reviews.models import MovieComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment
        fields = ('text', 'movie')
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
            'movie': forms.HiddenInput,
        }
