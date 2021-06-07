from django import forms 
from .models import pdf
class pdfForm(forms.ModelForm):  
    class Meta:  
        model = pdf
        fields = ('pdf_file','password')  
        widgets = {'password': forms.PasswordInput(),}
    
    def clean(self):
        pdffile=self.cleaned_data['pdf_file']
        file_extension=str(pdffile).split('.')
        if file_extension[1].lower()!= 'pdf':
            raise forms.ValidationError('FILE NOT SUPPORTED ! only pdf formets are allowed')  
        return self.cleaned_data    