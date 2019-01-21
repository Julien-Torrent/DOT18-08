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
    AllLedsOn =  bool(int(ledsStatus))
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
        return JsonResponse(commands.pop(0))
    else:
        return JsonResponse({'function':''})

# Turn Left of the requested angle
def turnLeft(request, angle):
    commands.append({'function' : "turnLeft", 'angle' : int(angle),'speed' : int(Speed)})
    return JsonResponse({'function' : "turnLeft", 'angle' : int(angle),'speed' : int(Speed)})

# Turn Right of the requested angle
def turnRight(request, angle):
    commands.append({'function' : "turnRight", 'angle' : int(angle),'speed' : int(Speed)})
    return JsonResponse({'function' : "turnRight", 'angle' : int(angle),'speed' : int(Speed)})

# getSpeed and add function name 'forward'
def forward(request):
    commands.append({'function' : "forward", 'speed' : int(Speed)})
    return JsonResponse({'function' : "forward", 'speed' : int(Speed)})

# getSpeed negates it and add function name 'backward'
def backward(request):
    commands.append({'function' : "backward", 'speed' : -int(Speed)})
    return JsonResponse({'function' : "backward", 'speed' : -int(Speed)})

# Allows the thimio to send sensor data to the server
# method = POST + data in data:
def sendStatus(request):
    if request.method == 'POST':
        #[{ "Name": "accéléromètre", "Value": 1, "TimeStamp": 12.221 }]
        # TODO save in DB if value is different
        for item in json.loads(request.body):
            print(item["Name"])
            print(item["Value"])
            print(item["TimeStamp"])

    return HttpResponse(status = 200)