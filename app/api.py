from django.http import HttpRequest
from django.template import RequestContext
from django.http import HttpResponse
from django.http import JsonResponse
import json

Mode = 0            # Current Mode 0=Manual, 1=FullForward, 2=Automatic
Speed = 0           # 0 to 1000 0=Stopped, 1000=Full Speed
AllLedsOn = False   # False = éteint, True = allumé

commands = list()

def setLeds(request, ledsStatus):
    global AllLedsOn
    AllLedsOn =  bool(ledsStatus)
    return HttpResponse(status=200)

def getLeds(request):
    global AllLedsOn
    return JsonResponse({'ledsOn' : AllLedsOn})

def setMode(request, mode):
    global Mode
    Mode = mode
    return HttpResponse(status=200)

def getMode(request):
    global Mode
    return JsonResponse({'mode' : Mode})


def setSpeed(request, speed):
    global Speed
    Speed = speed
    return HttpResponse(status=200)

def getSpeed(request):
    global Speed
    return JsonResponse({'speed': Speed})


# Thymio calls this to get the next action on Manual mode
def nextMove(request):
    if(len(commands)):
        res = commands[0]
        commands.pop(0)
        return JsonResponse(res)
    else:
        return JsonResponse({'function':''})


# getSpeed and add function name 'forward'
def forward(request):
    commands.append({'function' : "forward", 'speed' : int(Speed)})
    return JsonResponse({'function' : "forward", 'speed' : int(Speed)})

# getSpeed negates it and add function name 'backward'
def backward(request):
    commands.append({'function' : "backward", 'speed' : -int(Speed)})
    return JsonResponse({'function' : "backward", 'speed' : -int(Speed)})