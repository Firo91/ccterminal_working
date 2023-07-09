from django.db import models
from django.utils import timezone
from datetime import date, timedelta, datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission

class Meta:
    permissions = [
        ("can_access_bsm_equipment_search", "Can access BSM equipment search"),
    ]

class CustomUser(AbstractUser):
    username = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    
class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    bax_nr = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    tid = models.CharField(max_length=100)
    terminal_type = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    has_equipment = models.BooleanField(default=False)
    last_checked_date = models.DateField(null=True, blank=True)
    check_history = models.ManyToManyField('CheckHistory')
    last_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def is_check_expired(self):
        if self.last_checked_date:
            expiration_date = self.last_checked_date + timedelta(weeks=52)
            return date.today() > expiration_date
        return False
    
    def __str__(self):
        return self.name


class CheckHistory(models.Model):
    checked_by = models.CharField(max_length=100)
    checked_by_username = models.CharField(max_length=100)
    checked_date = models.DateTimeField()
    equipment_tid = models.CharField(max_length=100)
    equipment_id = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        to_field='id',  # Specify the foreign key to reference the tid field
    )
    equipment_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Checked by {self.checked_by} on {self.checked_date} on {self.equipment_name}"
        
class EquipmentEditHistory(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='edit_history')
    edited_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    edited_at = models.DateField(auto_now_add=True)
    field = models.CharField(max_length=255)
    old_value = models.CharField(max_length=255)

    class Meta:
        ordering = ['-edited_at']
