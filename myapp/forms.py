from django import forms

from study import settings
from .models import Student

Gender = [('Male','Male'),('Female','Female')]
class  NewStudent(forms.ModelForm):
    gender = forms.ChoiceField(choices=Gender)
    # dob = forms.DateField(
    #     widget = forms.DateInput(format='%d/%m/%Y',                                
    #                             attrs={'class':'form-control'}),
    #                             input_formats=settings.DATE_INPUT_FORMATS)
                                
                            
    class Meta:
        model = Student
        fields = ['name','course','rollno','dob','gender','email','mobile','guardian_mobile']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'course' : forms.TextInput(attrs={'class':'form-control'}),
            'rollno' : forms.TextInput(attrs={'class':'form-control'}),
            
            'dob' : forms.DateInput(attrs={'class':'form-control'}),
            
            #'gender' : forms.TextInput(attrs={'class':'form-control'}),
            'gender' : forms.RadioSelect(choices=Gender),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'mobile' : forms.TextInput(attrs={'class':'form-control'}),
            'guardian_mobile' : forms.TextInput(attrs={'class':'form-control'}),
        }
      
        
