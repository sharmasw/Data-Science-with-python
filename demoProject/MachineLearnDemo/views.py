from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
# def index(request):
#     return HttpResponse('a')

def index(request):
    context={'a':1}
    return render(request, 'startpage.html', context)

# def index(request):
#     return JsonResponse({'a':1})