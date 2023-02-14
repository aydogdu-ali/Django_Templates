from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Student

from .forms import StudentForm

# Create your views here.
def home(request):
    # return HttpResponse('<h1>Hello</h1>')
    #context dict yapısında olacak

    context = {
        'title':'ali',
        'desc': 'this is home',
        'number': 1111,
        'list1': ['a', 1, 'b', ['c', 2]],
        'dict1': {
            'key1': 'value1',
            'key2': 'value2',
        }
    }


    return render(request,'students/home.html', context)


'''
{{variables }}

{%command %- for döngüsü yazabiliriz.}

| >>> filter olarak kullanılır.

'''



#listeleme
def student_list(request):
    students = Student.objects.all()
    context = {
'students': students
    }

    return render(request, 'students/student_list.html', context)

#form veri gönderme
def student_add(request):
    form = StudentForm()

    if request.method =='POST':
        print(request.POST)
        print(request.FILES)
        form =StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('list')



    context = {
        'form':form
    }

    return render(request, 'students/student_add.html', context)



def student_update(request,id):

    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance= student)


    if request.method =='POST':
        form = StudentForm(request.POST,request.FILES, instance=student)

        if form.is_valid():
            form.save()
            return redirect('list')

    context = {
        'form': form
    }

    return render(request, 'students/student_update.html', context)

#detaylı öğrenci bilgisi
def student_detail(request,id):
    student = get_object_or_404(Student, id=id)

    context = {

        'student': student
    }

    return render (request, 'students/student_detail.html',context)


#silme işlemi 
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('list')

    context = {

        'student': student
    }

    return render (request, 'students/student_delete.html',context)