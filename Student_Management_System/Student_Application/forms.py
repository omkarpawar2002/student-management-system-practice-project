from django import forms
from .models import Student

gender_choices = [
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHER','OTHER')
]

subjects_choices = [
    ('PHY','PHYSICS'),
    ('CHE','CHEMISTRY'),
    ('MATH','MATHEMATICS'),
    ('BOTONY','BOTONY'),
    ('ZOOLOGY','ZOOLOGY'),
    ('CS','COMPUTER SCIENCE')
]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'student_id':'STUDENT ID',
            'first_name':'FIRST NAME',
            'last_name':'LAST NAME',
            'age':'AGE',
            'gender':'GENDER',
            'mobile_number':'MOBILE NUMBER',
            'city':'CITY',
            'address':'ADDRESS',
            'subject':'SUBJECT',
            'subject_image':'IMG',
            'email':'EMAIL ID',
            'password':'PASSWORD',
            'eligible':'ELIGIBILITY'
        }
        widgets = {
            'student_id':forms.NumberInput(attrs={
                'placeholder':'E.g.,101'
            }),
            'first_name':forms.TextInput(attrs={
                'placeholder':'Enter First Name'
            }),
            'last_name':forms.TextInput(attrs={
                'placeholder':'Enter Last Name'
            }),
            'gender':forms.RadioSelect(choices=gender_choices),
            'mobile_number':forms.TextInput(attrs={
                'placeholder':'+91 **********'
            }),
            'city':forms.TextInput(attrs={
                'placeholder':'E.g., Pune'
            }),
            'address':forms.Textarea(attrs={
                'placeholder':'E.g., Mumbai Maharashtra',
                'rows':'2'
            }),
            'subject':forms.Select(choices=subjects_choices),
            'subject_image':forms.FileInput(attrs={
                'type':'file'
            }),
            'email':forms.EmailInput(attrs={
                'placeholder':'youremail@gmail.com'
            }),
            'password':forms.PasswordInput(attrs={
                'type':'password'
            })
        }