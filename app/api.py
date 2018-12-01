from django.http import HttpRequest
from django.template import RequestContext
from django.http import HttpResponse
from django.http import JsonResponse

def forward(request):
    return JsonResponse({'function':'forward','parameters':[100] })
