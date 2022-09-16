
# from tkinter import Widget
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-feild'
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'content', 'status', 'header_image')
        # fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',  'placeholder':'set your blogs title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'show', 'type': 'hidden'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }

class EditForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content')
        # fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'set your blogs title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            # 'status': forms.Select(attrs={'class': 'form-control'}),

        }


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'body')

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),			
			
		}