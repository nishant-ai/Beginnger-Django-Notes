from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.
class EmployeeRange(models.Model):
    er_id = models.IntegerField(validators=[MinValueValidator(0)])
    er_code = models.CharField(max_length=15)
    er_display_text = models.CharField(max_length=50)
    er_min_no = models.IntegerField()
    er_max_no = models.IntegerField()
    er_created_timestamp = models.DateField(default=timezone.now)
    er_updated_timestamp = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Employee Range Custom Name"
        verbose_name_plural = "Employee Range Custom Name Plural"
        
    def __str__(self):
        return self.er_code
    
class Task(models.Model):
    # qs = EmployeeRange.objects.filter(er_code='ER0098')
    assigned_to = models.ForeignKey(EmployeeRange, on_delete=models.CASCADE) #MANY2ONE
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task_name
    
class Development(models.Model):
    project_name = models.CharField(max_length=120)
    project_description = models.TextField(blank=True, null=True)
    assigned_to = models.ManyToManyField(EmployeeRange)
    
    def __str__(self):
        return self.project_name
    