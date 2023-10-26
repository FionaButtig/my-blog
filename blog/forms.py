from django import forms
from .models import Post

# forms.ModelForm will tell Django to do some of the work for us
class PostForm(forms.ModelForm):

    # tells Django what Model should be used for this form
    class Meta:
        model = Post
        # what fields should end up in the form
        # cus when u edit the form u wanna change either the titel or text so this tells django to put in a small textfield for title and a large one for text
        fields = ('title', 'text',)