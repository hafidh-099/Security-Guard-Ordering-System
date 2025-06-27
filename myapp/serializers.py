from rest_framework import serializers
from .models import Order, Organization, SecurityOffice, ArmedSecurityGuard

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class SecurityOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityOffice
        fields = '__all__'

class ArmedSecurityGuardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArmedSecurityGuard
        fields = '__all__'
