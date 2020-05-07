from django.shortcuts import render
from django.http import HttpResponse

from .process.process import  __init__process
# Create your views here.

def index(request):
    __init__process()
    return HttpResponse()
