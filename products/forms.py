from .models import Product
from django import forms

class NewProductForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple':True}), required=False)
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'address', 'category', 'phone_number', 'tg_username')
    
    def save(self, request, commit=True):
        product = self.instance
        product.author = request.user   
        super().save(commit)
        return product 
    
class ProductForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple':True}), required=False)
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'address', 'category', 'phone_number', 'tg_username')
    
  
    