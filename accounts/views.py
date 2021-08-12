from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from knox.models import AuthToken
from rest_framework import  status
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login

# Create your views here.

class RegisterAPI(GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self,request):
        
        serializer = self.get_serializer(data =request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                
                'user':RegisterSerializer(user,context= self.get_serializer_context()).data,
                
                'token' : AuthToken.objects.create(user)[1]
            },status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class LoginAPI(KnoxLoginView):    
    
    permission_classes = (permissions.AllowAny,)
    
    def post(self,request,format = None):
        serializer = AuthTokenSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request,user)
            return super(LoginAPI,self).post(request,format=None)
        
            
    

    