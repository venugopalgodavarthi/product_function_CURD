from django import forms
from online.models import * 

class itemsform(forms.ModelForm):
    class Meta:
        model = itemsmodel
        fields = '__all__'
        
class productform(forms.ModelForm):
    class Meta:
        model =productmodel
        fields = '__all__'