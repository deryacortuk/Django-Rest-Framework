from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style = {'input_type':'password'},write_only=True)
    password2 = serializers.CharField(style ={'input_type':'password'},write_only =True)  
    
    class Meta:
        model = User
        fields = ['username','email','password','password2']
        
        
    def save(self):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match.'})
        user.set_password(password)
        user.save()
        return user
    
