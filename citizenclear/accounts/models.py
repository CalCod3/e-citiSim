from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator


class UserManager(BaseUserManager):
    

    def create_user(self, first_name:str, last_name:str, email:str, id_number:int, password:None, is_staff:False, is_superuser:False)->"User":
        if not email:
            raise ValueError("Please provide a valid e-mail address")
        if not first_name:
            raise ValueError("Please provide a valid First Name")
        if not last_name:
            raise ValueError("Please provide a valid Last Name")
        if not id_number:
            raise ValueError("Please provide a valid ID Number")
        
        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.id_number = id_number
        user.set_password(password)
        user.is_active = True
        user.is_superuser = is_superuser
        user.is_staff = is_staff
        user.save()
        return user


    def create_superuser(self, first_name:str, last_name:str, email:str, id_number:int, password:str)->"User":
        if not email:
            raise ValueError("Please provide a valid e-mail address")
        if not first_name:
            raise ValueError("Please provide a valid First Name")
        if not last_name:
            raise ValueError("Please provide a valid Last Name")
        if not id_number:
            raise ValueError("Please provide a valid ID Number")
        
        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.id_number = id_number
        user.set_password(password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()

        


        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    id_number = models.IntegerField(validators=[MinValueValidator(100000), MaxValueValidator(10000000000)])
    password = models.CharField(max_length=255)
    username = None

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "id_number"]

class Appointment(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    date_time = models.DateTimeField(unique=True)

    

    class Meta:
        verbose_name = ("Appointment")
        verbose_name_plural = ("Appointments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Appointment_detail", kwargs={"pk": self.pk})
