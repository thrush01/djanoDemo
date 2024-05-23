from django import forms

from .models import Item

INPUT_CLASSES='w-fully py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):

    class Meta:
        model= Item
        fields=('category','name', 'description', 'price','image',)

        widgets={
                'category':forms.Select(attrs={
                    'class':'w-fully py-4 px-6 rounded-xl border'
                }),
                'name':forms.TextInput(attrs={
                    'class':'w-fully py-4 px-6 rounded-xl border'
                }),
                'description':forms.TextInput(attrs={
                    'class':'w-fully py-4 px-6 rounded-xl border'
                }),
                'price':forms.TextInput(attrs={
                    'class':'w-fully py-4 px-6 rounded-xl border'
                }),
                'image':forms.FileInput(attrs={
                    'class':'w-fully py-4 px-6 rounded-xl border'
                }),
            }
