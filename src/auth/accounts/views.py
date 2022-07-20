from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer


class RegistrateView(APIView):

    def get(self, request):
        return render(request=request, template_name='registrate/registrate.html')

    def post(self, request):
        data = {
            'username': request.POST.dict()['username'],
            'password': request.POST.dict()['password'],
        }
        userserializer = CustomUserSerializer(data=data)
        if userserializer.is_valid():
            validated_data = userserializer.validated_data
            user = userserializer.create(validated_data=userserializer.validated_data)
            return redirect('/login/')
        return redirect('/registrate/')


class LoginView(APIView):

    def get(self, request):
        return render(request=request, template_name='login/login.html')

    def post(self, request):
        username = request.POST.dict()['username']
        password = request.POST.dict()['password']
        user = authenticate(request=request, username=username, password=password,)
        if user:
            login(request=request, user=user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/main/')
        return redirect('/login/')


class LogoutView(APIView):
    def get(self, request):
        logout(request=request)
        return redirect('/login/')


class MainView(APIView):
    def get(self, request):
        return render(request=request, template_name='main/main.html', context={'username': request.user.username})
