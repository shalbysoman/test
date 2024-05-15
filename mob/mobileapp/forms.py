from django import forms

from .models import Book, Author


class AuthorForm(forms.ModelForm):

    class Meta:
        model=Author
        fields=['name']
        widgets={
            'name':forms.TextInput(attrs={'class':'from-control','placeholder':'enter book author name'})
        }



class BookForm(forms.ModelForm):

    class Meta:

        model=Book
        fields='__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the book name'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter the authors name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the book price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the book quantity'}),


        }