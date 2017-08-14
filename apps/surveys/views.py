from django.shortcuts import render, HttpResponse, redirect

# the index function is called when root is visited
def index(request):
    return render(request, "surveys/index.html")

def process(request):
    # Add logic
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def result(request):
    # Add logic
    response = "Hello, I am your first request!"
    return HttpResponse(response)