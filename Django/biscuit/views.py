from django.shortcuts import render

# Create your views here.
def all_biscuit(request):
    return render(request, 'biscuit/all_biscuit.html')