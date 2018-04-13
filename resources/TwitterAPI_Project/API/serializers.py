from rest_framework import serializers
from .models import Apı_class

class Apı_Classserializer(serializers.ModelSerializer):
    class Meta:
        model = Apı_class
        #fields =('content')
        fields='__all__'