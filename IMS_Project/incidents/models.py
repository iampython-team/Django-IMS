from django.db import models
from datetime import datetime

# Create your models here.
# incident - > incident_id,i proprity, i assignedto,status, i dec, i dataraised
# table name = appname_modelname

SEVERITY_LEVEL=[
    ('Critical','C'),
    ('HIGH','H'),
    ('MEDIUM','M'),
    ('LOW','L')       
]

I_STATUS=[
    ('Open','O'),
    ('In Progress','I'),
    ('Closed','C')  
]

class IncidentCategory(models.Model):
    incident_category_name=models.CharField(max_length=50)
    incident_category_slug=models.SlugField(max_length=50)
    
    def __str__(self):
        return self.incident_category_name
        

class Incident(models.Model):
    incident_category= models.ForeignKey('IncidentCategory',related_name='incidentcategory',on_delete=models.CASCADE)
    incident_title=models.CharField(max_length=50)
    incident_id=models.IntegerField()
    incident_slug=models.SlugField(max_length=50)
    incident_description=models.CharField(max_length=200)
    incident_image=models.ImageField(upload_to='images/')
    incident_severity=models.CharField(max_length=10,choices=SEVERITY_LEVEL)
    incident_assigned=models.CharField(max_length=40)
    incident_status=models.CharField(max_length=20,choices=I_STATUS)
    incident_date=models.DateField(default=datetime.now)
 
    
    def __str__(self):
        return self.incident_severity
  
  
class Contact(models.Model):
    name=models.CharField(max_length=50)
    emai=models.EmailField(help_text='enter your email .com')
    subject=models.TextField()
    mobile=models.IntegerField()
    
    
    
    
    
    
    
 
  
    


    
