from django import forms
from .models import StudentsInfo

class StdForm(forms.ModelForm):
    class Meta:
        model = StudentsInfo
        fields = '__all__'
        labels = {
            'student_id': 'Student ID',
            'name': 'Name',
            'email': 'Email',
            'gender': 'Gender',
            'phone': 'Phone Number',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter Student Name...', 'class': 'form-control'}),
            'email': forms.EmailInput( #CharInput / EmailInput
                attrs={'placeholder': 'Enter student Email...', 'class': 'form-control'}),
            'gender': forms.Select(
                attrs={'class': 'form-control'}),
            'phone': forms.TextInput(
                attrs={'placeholder': 'Enter student Phone...', 'class': 'form-control'}),
        }
