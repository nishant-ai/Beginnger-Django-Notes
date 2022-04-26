from django.db import models

# Create your models here.
class EmployeeRange(models.Model):
    er_id = models.IntegerField()
    er_code = models.CharField(max_length=15)
    er_display_text = models.CharField(max_length=50)
    er_min_no = models.IntegerField()
    er_max_no = models.IntegerField()
    er_created_timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    er_updated_timestamp = models.DateTimeField(auto_now_add=True)