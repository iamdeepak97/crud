from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['ename', 'address', 'position', 'salary']
    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['ename'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Employee Name'})
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Address'})
        self.fields['position'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Position'})
        self.fields['salary'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Salary'})
