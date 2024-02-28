from rest_framework import serializers
from tekken.models import Tekken

class TekkenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tekken
        fields = '__all__'