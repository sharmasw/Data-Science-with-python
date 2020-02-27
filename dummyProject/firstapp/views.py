from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.


# def index(requests):
#     return HttpResponse('Hello World! 2')



def index(requests):
    return JsonResponse({'a':1})