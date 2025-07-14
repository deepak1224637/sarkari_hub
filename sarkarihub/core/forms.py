from django import forms
from core.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'link']
        widgets = {
            'category': forms.Select(choices=Post.CATEGORY_CHOICES),
        }
