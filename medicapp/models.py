from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Medical(models.Model):
    s1 = models.CharField(max_length=200)
    s2 = models.CharField(max_length=200)
    s3 = models.CharField(max_length=200)
    s4 = models.CharField(max_length=200)
    s5 = models.CharField(max_length=200)
    disease = models.CharField(max_length=200)
    medicine = models.CharField(max_length=200)
    patient = models.ForeignKey(User, related_name="patient", on_delete= models.CASCADE)
    doctor = models.ForeignKey(User, related_name="doctor", on_delete= models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.disease



class Treatment(models.Model):
    approved = models.BooleanField(default=False)
    time = models.CharField(max_length=200, null=True)
    patient = models.ForeignKey(User, related_name="pat", on_delete= models.CASCADE)
    doctor = models.ForeignKey(User, related_name="dor", on_delete= models.CASCADE, null=True)
    treatment_day = models.DateTimeField(null=True)
    medical = models.ForeignKey(Medical, related_name="medical", on_delete= models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.approved



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)  # Add a default value
    birth_date = models.DateField(default='None')
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])

    def __str__(self):
        return f"Profile for {self.user.username}"



