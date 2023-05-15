from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company , Employee
from api.serializers import CompanySerializer , EmployeeSerializer
from rest_framework.decorators import action 
from rest_framework.response import Response 
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    #companies/{company_id}/employees 
    @action(detail = True, methods=['get']) #detail true matlab pk pass krna is zaruri 
    def employees(self,request,pk=None): #pk is company ki pk 
        try:
            company=Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            # serialize emp  
            emps_serializer = EmployeeSerializer(emps,many=True,context = {'request': request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message': 'company might not exist!'
            })
        # pass 

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class= EmployeeSerializer 

