from django.shortcuts import render
from django.http import *
from lib.player import getPlayerUrl

# Create your views here.

def player(request):
    playerid = ''
    if request.method == 'get' or request.method == 'GET':
        playerid = request.GET.get('playerid', '')
        print playerid
        return HttpResponseRedirect(redirect_to=getPlayerUrl(playerid))
    if not playerid:
        return render(request, 'frontPage.html')

def index(request):
	return render(request, 'frontPage.html')
