from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("Hello World")

def about(request):
    return HttpResponse("Welcome to Joshua's World")

def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}")

def sum(request, num1, num2):
    return HttpResponse(f"num1 is {num1}, num2 is {num2}, the total number is {num1+num2}")