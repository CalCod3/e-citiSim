from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator


class UserManager(BaseUserManager):
    

    def create_user(self, first_name:str, last_name:str, email:str, id_number:int, password:None)->"User":
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
        user.save(using = self._db)
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
        user.save(using = self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    id_number = models.IntegerField(validators=[MinValueValidator(100000), MaxValueValidator(10000000000)])
    password = models.CharField(max_length=255)
    username = None
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "id_number"]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, accounts):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def get_absolute_url(self):
        return reverse("User-detail", kwargs={"pk": self.pk})

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
