from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from .serializers import UserSerializer, LoginSerializer, PasswordChangeSerializer
from django.db import transaction

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key,
            'message': 'User registered successfully',
            'redirect': '/three'
        }, status=status.HTTP_201_CREATED, headers=headers)


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserInfoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    """ Authorizedの状況をプリント """

    def get(self, request):


        if request.user.is_authenticated:
            print(Response)
            return Response({
                'username': request.user.username,
                'email': request.user.email,
                'id': request.user.id,
                
                # 必要に応じて他のフィールドも追加
            })
            
        else:
            return Response({"detail": "認証に失敗しました。"}, status=status.HTTP_401_UNAUTHORIZED)

    
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password'],
                
            )
            if user:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user': UserSerializer(user).data,
                    'redirect': '/three'
                })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        if request.auth:
            request.auth.delete()  # トークンを削除（TokenAuthentication使用時）
        logout(request)
        return Response({
            'detail': 'Successfully logged out.',
            'clear_cookie': 'auth_token'
        }, status=status.HTTP_200_OK)

class PasswordChangeView(generics.UpdateAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.object = self.get_object()
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
