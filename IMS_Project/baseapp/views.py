from django.shortcuts import render
from django.http import HttpResponse


# function based views ------ first parameter django function based views request
# class based views ----

# Create your views here.
def index(request):
    return render(request,'index.html')



