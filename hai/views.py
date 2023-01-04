from django.shortcuts import render

# Create your views here.
def yeah(request):
    return render(request, 'yeah1.html')