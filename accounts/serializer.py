from rest_framework import serializers
from rest_framework.authtoken.models import Token

class TokenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'

class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()