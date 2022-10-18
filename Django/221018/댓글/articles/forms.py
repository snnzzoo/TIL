from django import forms
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        labels = {
            'title': '제목',
            'coontent': '내용',
            'image': '이미지',
        }