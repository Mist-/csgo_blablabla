from django.shortcuts import render
from django.http import *
from lib.player import getPlayerUrl
from lib.scraper import getPlayerInfo

# Create your views here.

def playerinfo(request):
    playerid = ''
    if request.method == 'get' or request.method == 'GET':
        playerid = request.GET.get('playerid', '')
        playerid = getPlayerUrl(playerid)
    if not playerid:
        return {
            error: 1,
        }
    else:
        return getPlayerInfo(playerid=playerid)

def player(request):
    return render(request, 'search.html')

def index(request):
	return render(request, 'frontPage.html')
