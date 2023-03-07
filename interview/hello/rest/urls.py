
from django.urls import path
from .views import StudentListView , studentDetailView

urlpatterns = [
    path('stud/', StudentListView.as_view()),
    path('stud/<int:pk>/', studentDetailView.as_view()),
    
]