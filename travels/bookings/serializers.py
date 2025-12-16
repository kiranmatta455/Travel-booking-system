# Correct import - it's "rest_framework" not "restframework"
from rest_framework import serializers  # lowercase 's'
from .models import Bus, Seat  # Import both models
from django.contrib.auth.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        models = User
        fields = ['username', 'email', 'password']

    def create(self, validate_date):
        user = User.objects.create_user(
            username = validate_date['username'],
            email = validate_date['email'],
            password = validate_date['password']
        )
        return user

class BusSerializer(serializers.ModelSerializer):  # Capital M, capital S
    class Meta:
        model = Bus
        # Remove the dash - it should be either '__all__' or a list of fields
        fields = '__all__'  # OR fields = ['field1', 'field2', ...]

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'seat_number', 'is_booked']  # Single underscore, not double