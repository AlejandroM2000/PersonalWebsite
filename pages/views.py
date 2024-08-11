from django.shortcuts import render

def home(request):
    return render(request, "pages/page.html", {})
# Create your views here.
