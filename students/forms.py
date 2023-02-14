from django import forms
from .models import Student

#formlar ile çalışırken bu yapıyı kullanıyoruz. ModelForm yapısını



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'



    



# fields = (
#     'id',
#     'first_name',
#     'last_name',
#     'image'
# )