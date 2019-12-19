from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from incidents.models import Incident
from django.db.models import Max,Min,Avg,Sum
from .forms import PersonForm,ContactForm

# Create your views here.
# two types - function based and class based 

def list_incident(request):
    all_incidents=Incident.objects.all() # select * from incidents_incident 
    all_incidents_count=Incident.objects.count() #select count(*) from incidents_incident 
    context = {
        'allincidents' : all_incidents,
        'incident_count':all_incidents_count
    }
    return render(request,'incidents.html',context)


def list_incident_details(request,id):
    incident_details=Incident.objects.filter(incident_slug=id).select_related()
    context={
        'incident_details':incident_details
    }
    return render(request,'incident_details.html',context)

def all_queries(request):
    max_incident_number=Incident.objects.all().aggregate(Max('incident_id'))
    sum_incident_number=Incident.objects.all().aggregate(Sum('incident_id'))
    
    second_largest_row=Incident.objects.order_by('-incident_date')[1]
    
    get_incident = Incident.objects.filter(
        incident_title__istartswith='I',
        incident_category__incident_category_name__startswith='T'
    )
    
    get_distinct_Incident=Incident.objects.distinct('incident_severity').order_by('-incident_severity')
      
    context={
        'max_incident_number':max_incident_number,
        'sum_incident_number':sum_incident_number,
        'second_largest_row':second_largest_row,
        'get_incident':get_incident,
        'get_distinct_Incident':get_distinct_Incident
    }
    
    return render(request,'allqueries.html',context)

def personform(request):
    if request.method == 'POST':
        form=PersonForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/incidents/')
    else:
        form=PersonForm()
    
    return render(request,'person/personform.html',{'pform':form})


def contactform(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('you are successfully submitted')
        
    else:
        form=ContactForm()
        
    return render(request,'person/contactform.html',{'cform':form})
    
        



