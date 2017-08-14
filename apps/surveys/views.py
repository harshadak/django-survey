from django.shortcuts import render, HttpResponse, redirect

# the index function is called when root is visited
def index(request):
    return render(request, "surveys/index.html")

def process(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        if "counter" in request.session:
            request.session['counter'] += 1
        else:
            request.session['counter'] = 1
        return redirect("/surveys/result")

def result(request):
    return render(request, "surveys/result.html")

def reset(request):
    try:
        del request.session['counter']
        return redirect("/")
    except:
        return redirect("/")