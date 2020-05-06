from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def hello(request):
    # return HttpResponse("Hello World ! ");
    context = {}
    context['hello'] = 'hello word!'
    context['if_flag'] = 1
    return render(request, 'hello.html', context)