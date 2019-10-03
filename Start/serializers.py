from rest_framework import serializers
from .models import  data

class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model=data
        fields=['id','Name','Email','Cource','Sem','Subjects','Query']