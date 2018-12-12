from django.http import HttpRequest
from django.template import RequestContext
from django.http import HttpResponse
from django.http import JsonResponse
import json

Mode = 0            # Current Mode 0=Manual, 1=FullForward, 2=Automatic
Speed = 0           # 0 to 1000 0=Stopped, 1000=Full Speed
AllLedsOn = False   # False = eteint, True = allumé

def setLeds(request, ledsStatus):
    global AllLedsOn
    AllLedsOn =  bool(ledsStatus)
    return HttpResponse(status=200)

def getLeds(request):
    global AllLedsOn
    return JsonResponse({'LedsOn' : AllLedsOn})

def setMode(request, mode):
    global Mode
    Mode = mode
    return HttpResponse(status=200)

def getMode(request):
    global Mode
    return JsonResponse({'Mode' : Mode})


def setSpeed(request, speed):
    global Speed
    Speed = speed
    return HttpResponse(status=200)

def getSpeed(request):
    global Speed
    return JsonResponse({'Speed': Speed})


# getSpeed and add function name 'forward'
def forward(request):
    errors_dict = json.loads(getSpeed(request).content)

    errors_dict["Function"] = "forward"

    return JsonResponse(errors_dict)

# getSpeed negates it and add function name 'backward'
def backward(request):
    errors_dict = json.loads(getSpeed(request).content)

    errors_dict["Speed"] = -int(errors_dict["Speed"]);
    errors_dict["Function"] = "backward"

    return JsonResponse(errors_dict)