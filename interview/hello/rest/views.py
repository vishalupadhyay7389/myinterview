from django.shortcuts import render
from rest_framework .views import APIView
from.models import Student , StudentSerializer
from rest_framework .response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import authentication


# Create your views here.

class StudentListView(APIView):
    def get(self,request):
        stud = Student.objects.all()
        studSer = StudentSerializer(stud , many = True)
        return Response(studSer.data)
    
    def post(self,request):
        studSerializer = StudentSerializer(data = request.data)
        if studSerializer.is_valid():
            studSerializer.save()
            return Response (studSerializer.data  , status= status.HTTP_201_CREATED)
        return Response(studSerializer.errors)
    
class studentDetailView(APIView):
    
    def get_course(self ,pk):
        try:
            return Student.objects.get(pk = pk)
        except stud.DoesNotExits:
            raise Http404
            
        

    def get(self, request , pk):
        studend = self.get_course(pk)
        studSerlizer = StudentSerializer(studend)
        return Response(studSerlizer.data)
    
    def post(self,request):
        studSerializer = StudentSerializer(data = request.data)
        if studSerializer.is_valid():
            name=


            
            return Response (studSerializer.data  , status= status.HTTP_201_CREATED)
        return Response(studSerializer.errors)
    


    def put(self,request,pk):

        studend = self.get_course(pk)
        studSerlizer = StudentSerializer(studend , data=request.data)
        if studSerlizer.is_valid():
            studSerlizer.save()
            return Response(studSerlizer.data , status= status.HTTP_201_CREATED)
        return Response(studSerlizer.errors)
        

    def delete(self , request,pk):
        self.get_course(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


           
        

        

    
