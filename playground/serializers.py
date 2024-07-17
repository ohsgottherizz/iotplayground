from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Child, Reservation, PlaygroundOccupancy

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['id', 'name']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'child', 'time']

class PlaygroundOccupancySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaygroundOccupancy
        fields = ['id', 'level', 'timestamp']