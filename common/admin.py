from django.contrib import admin
from .models import EmployeeRange, Task, Development

# Register your models here.
class EmployeeRangeAdmin(admin.ModelAdmin):
    list_display = ('er_id', 'er_code', 'er_display_text', 'er_created_timestamp')
    
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'assigned_to', 'date_added')

admin.site.register(EmployeeRange, EmployeeRangeAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Development)