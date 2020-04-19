from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'layout.html')

def new_search(request):
    return render(request,'my_app/new_search.html')
