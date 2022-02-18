from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import  render, redirect
# from django.contrib.auth import login, authenticate, logout
# from django.contrib import messages
# from django.contrib.auth.forms import AuthenticationForm
# from django.views.decorators.csrf import csrf_exempt

from .models import Player
from .serializers import PlayerSerializer
# from .forms import NewUserForm

# Create your views here.
class PlayerViewSet(viewsets.ViewSet):
    
    def list(self, request):
        # /api/player
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def create(self, request):
        # /api/player
        serializer = PlayerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        check = serializer.validated_data
        if(check['won'] + check['loss'] + check['ties'] != check['played']):
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        # /api/player/<int:pk>
        player = Player.objects.get(id=pk)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # /api/player/<int:pk>
        player = Player.objects.get(id=pk)
        serializer = PlayerSerializer(instance=player, data=request.data)
        serializer.is_valid(raise_exception=True)
        
        check = serializer.validated_data
        if(check['won'] + check['loss'] + check['ties'] != check['played']):
            return Response(status=status.HTTP_304_NOT_MODIFIED)
            
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        # /api/player/<int:pk>
        if(pk < 3):
            return Response(status=status.HTTP_403_FORBIDDEN)
        player = Player.objects.get(id=pk)
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def RPSView(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')
    return render(request, "rockpaperscissors.html")

def coinView(request):
    return render(request, "coin.html")

# def register_request(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful." )
#             return redirect("homepage")
#     messages.error(request, "Unsuccessful registration. Invalid information.")
#     form = NewUserForm()
#     return render (request=request, template_name="player/register.html", context={"register_form":form})

# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("homepage")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="player/login.html", context={"login_form":form})

# def logout_request(request):
# 	logout(request)
# 	messages.info(request, "You have successfully logged out.") 
# 	return redirect("homepage")

def homeView(request):
    return render(request, "home.html")

