from rest_framework import serializers
from .models import Recommendations

class RecSysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendations
        fields = ['movie_name']
