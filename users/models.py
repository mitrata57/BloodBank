from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
BLOOD_GROUPS = [
    ('A+', 'A+'), ('A-', 'A-'),
    ('B+', 'B+'), ('B-', 'B-'),
    ('AB+', 'AB+'), ('AB-', 'AB-'),
    ('O+', 'O+'), ('O-', 'O-'),

]
#Custom User Model
class CustomUser(AbstractUser):
    CHOILCES = [
        ('donor','Donor'),
        ('recipent','Recipient'),
        ('hospital','Hospital'),
        ('admin','Admin')

    ]
    role = models.CharField(max_length = 20 , choices = CHOILCES)
    phone_number = models.CharField(max_length=15,)
    address = models.TextField()
    def __str__(self):
        return f"{self.username}[{self.role}]"
   


class Donor(models.Model):
    user = models.OneToOneField(CustomUser , on_delete = models.CASCADE)
    blood_group =models.CharField(max_length=3 , choices=BLOOD_GROUPS)
    medical_document = models.FileField(upload_to="donors/documents")


class Receipient(models.Model):
    user = models.OneToOneField(CustomUser , on_delete = models.CASCADE)
    blood_group =models.CharField(max_length=3 , choices=BLOOD_GROUPS)
    medical_document = models.FileField(upload_to="receipient/documents")
    

        
    
    
