from django.http import HttpRequest
from django.template import RequestContext
from django.http import HttpResponse
from django.http import JsonResponse

Mode = 0    # Current Mode 0=Manual, 1=FullForward, 2=Automatic
Speed = 0   # 0 to 1000 0=Stopped, 1000=Full Speed

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