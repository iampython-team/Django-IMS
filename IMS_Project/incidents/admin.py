from django.contrib import admin
from incidents.models import Incident,IncidentCategory

# Register your models here.

class IncidentAdmin(admin.ModelAdmin):
    list_display=('incident_id','incident_severity','incident_assigned','incident_status','incident_date')
    prepopulated_fields={'incident_slug':('incident_title',)}
    
admin.site.register(Incident,IncidentAdmin)


class IncidentCategoryAdmin(admin.ModelAdmin):
    list_display=('incident_category_name',)
    prepopulated_fields={'incident_category_slug':('incident_category_name',)}
    
    
    
admin.site.register(IncidentCategory,IncidentCategoryAdmin)
