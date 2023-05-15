# creating serailizers here  
from rest_framework import serializers 
from api.models import Company , Employee
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    # company is will now be only read and not changed 
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company 
        fields = "__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee 
        fields = "__all__" # or pass a list 
        