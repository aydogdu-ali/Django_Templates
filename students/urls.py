

from django.urls import path
from .views import(
 home,
student_list, 
student_add,
student_update,
student_detail,
student_delete)

urlpatterns = [
    path('', home, name='home'),
    path('list/', student_list, name='list'),
    path('add/', student_add, name='add'),
    path('update/<int:id>/', student_update, name='update'),
    path('detail/<int:id>/', student_detail, name='detail'),
     path('delete/<int:id>/', student_delete, name='delete'),
]
