from . models import Item , Comment
from django import forms

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields= ['name', 'description', 'price', 'image']

# online_app/forms.py (Add this class)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ['text']