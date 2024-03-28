from functools import partial
from telnetlib import GA
from turtle import title
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from journeyapp.models import Game, WishList
from . import serializers
from rest_framework import status
from .serializers import *

@api_view(["GET"])
def testResponse (request):
    return Response({"message":"successfully sent"})

@api_view(["POST"])
def add_game(request):
    if request.method =="POST":
        game_title = request.data.get("title")
        
        if Game.objects.filter(title=game_title).exists():
            return Response({"message":"Game already added"})
        else :
            serializer = GameSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Game has been added"},status=201)
        return Response(serializer.errors,status=400)

@api_view(["GET"])
def all_games (request):
    games = Game.objects.all().order_by("-date_finished")
    count = games.count()
    serializer = GameSerializer(games,many=True)
    data =  { "count":count , "games": serializer.data}
    return Response(data)

@api_view(["GET"])
def game_detail(request,game_id):
    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        raise Http404("Game does not exist")
    serializer =GameSerializer(game)
    return Response(serializer.data)


@api_view(["GET"])
def search_game(request):
    games = Game.objects.filter(title__icontains=request.GET.get("search")).order_by("-date_finished")
    serializer = GameSerializer(games,many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def remove_game(request,game_id):
    try:
        game = Game.objects.get(id=game_id)
        game.delete();    
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Game.DoesNotExist:
        raise Http404("Game doesn't Exist")

@api_view(["POST"])
def add_wishlist(request):
    if request.method =="POST":
        game_title = request.data.get("title")
        if WishList.objects.filter(title=game_title).exists():
            return Response({"message":"Already in Wish List"})
        else:
            serializer = WishListSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Added to Wish List"},status=201)
        return Response(serializer.errors,status=400)
    
@api_view(["GET"])
def show_wishlist (request):
    wishlist = WishList.objects.all().order_by("-date_wished")
    serializer = WishListSerializer(wishlist,many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def remove_wishlist(request,wish_id):
    try:
        game = WishList.objects.get(id=wish_id)
        game.delete();    
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Game.DoesNotExist:
        raise Http404("Game doesn't Exist")
    
    
@api_view(["PATCH"])
def markFavourite(request,game_id):
    try :
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        return Response({"message":"Game with that id doesn't exist"},status=404)
    serializer = GameSerializer(instance=game,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        game = Game.objects.all().order_by("-date_finished")
        new_data = GameSerializer(game,many=True)
        return Response(new_data.data)
    return Response(serializer.errors,status=400)

@api_view(["GET"])
def all_genres (request) :
    games = Game.objects.all()
    uncleaned_genre_list= [game.genre for game in games]
    unique_genres = set(uncleaned_genre_list)
    cleaned_genre_list = list(unique_genres)
    return JsonResponse({"genres":cleaned_genre_list})
    
@api_view(["GET"])
def filter_games(request,method,genreOption=""):
    
    if (method == "favourite") :
        game = Game.objects.filter(favourite=True).order_by("-date_finished")
        serializer = GameSerializer(game,many=True)
        return Response(serializer.data)
    
    elif(method == "all") :
        game = Game.objects.all().order_by("-date_finished")
        serializer = GameSerializer(game,many=True)
        return Response(serializer.data)
    
    elif (method == "title" or method == "-title"):
        game = Game.objects.all().order_by(method)
        serializer = GameSerializer(game,many=True)
        return Response(serializer.data)
    elif (method == 'genre'):
        game = Game.objects.filter(genre=genreOption)  
        serializer = GameSerializer(game,many=True)
        return Response(serializer.data)
    
@api_view(["PATCH"])
def add_opinion(request,game_id):
    game = Game.objects.get(id=game_id)
    serializer = GameSerializer(instance=game,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        new_data = GameSerializer(game)
        return Response(new_data.data)
    return Response(serializer.errors,status=400)