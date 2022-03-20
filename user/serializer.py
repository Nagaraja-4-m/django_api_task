from rest_framework import serializers
from .models import Userr

class UserrSerializer(serializers.ModelSerializer):
    class Meta:
        model=Userr
        fields=['user_id','first_name','last_name','mobile_number','email','created_at','updated_at']
    pass