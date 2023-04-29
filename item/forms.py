from django import forms
from .models import Item
shi = "form-control form-control-sm"
INPUT_CLASSES = 'form-select'
INPUT_CLASSES2="form-control"
INPUT_CLASSE3 = "form-floating"
INOUT='form-control form-control-sm'
class NewItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields=('category','name','description','price',
                'image','address')
        widgets = {
            'category':forms.Select(attrs={
            'class':INPUT_CLASSES
            }),
            'name':forms.TextInput(attrs={
            
            }),
            'description ':forms.TextInput(attrs={
            
            }),
            'price ':forms.TextInput(attrs={
            
            }),
            'image ':forms.FileInput(attrs={

            }),
            'address':forms.TextInput(attrs={
            
            }),
        }
class EditItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields=('name','description','price',
                'image','is_sold')
        widgets = {
            
            'name':forms.TextInput(attrs={
            
            }),
            'description ':forms.TextInput(attrs={
            
            }),
            'price ':forms.TextInput(attrs={
            
            }),
            'image ':forms.FileInput(attrs={
            'class' : 'form-control form-control-sm'
            
            
             
            }),
            'address':forms.TextInput(attrs={
            
            }),
            
        }        
    