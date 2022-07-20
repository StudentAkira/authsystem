from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import CustomUser


class RegistrateView(APIView):

    def get(self, request):
        return render(request=request, template_name='registrate/registrate.html')

    def post(self, request):
        username = request.POST.dict()['username']
        password = request.POST.dict()['password']
        user = CustomUser.objects.create_user(username, password)
        return Response({'username': user.username, 'password': user.password})


class LoginView(APIView):

    def get(self, request):
        return render(request=request, template_name='login/login.html')

    def post(self, request):
        username = request.POST.dict()['username']
        password = request.POST.dict()['password']
        user = authenticate(request=request, username=username, password=password, )
        login(request=request, user=user)
        return Response({'user': user.username, 'password': user.password})


class LogoutView(APIView):
    def get(self, request):
        logout(request=request)
        return redirect('/login/')


class MainView(APIView):
    def get(self, request):
        return render(request=request, template_name='main/main.html', context={'username': request.user.username})
