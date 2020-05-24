#accounts/serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    date_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('email', 'full_name', 'active', 'admin', 'staff')
        extra_kwargs = {'password': {'write_only' : True}}




