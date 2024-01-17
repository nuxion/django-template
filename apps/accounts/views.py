# from django.shortcuts import render
from django.shortcuts import render


# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the account index")
    return render(request, "accounts/index.html")
