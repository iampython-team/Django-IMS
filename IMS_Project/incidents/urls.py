from django.urls import path,include
from . import views

urlpatterns = [
    path('incidents/',views.list_incident,name='incidentsx'),
    path('incidents_deatails/<slug:id>',views.list_incident_details,name='incident_details'),
    path('allqueries/',views.all_queries,name='allq'),
    path('personform/',views.personform,name='person_form'),
    path('contactform/',views.contactform,name='contact_form'),
]


