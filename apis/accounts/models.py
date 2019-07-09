from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    ROLES=(("SA","Superadmin"), ("NA","Normaladmin"),("JA","Journalist"),("GU","Guestuser"))
    role= models.CharField(choices=ROLES,max_length=2)
    email=models.EmailField(max_length=50, unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=('username', 'password')

class profile(models.Model):
    User= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dob= models.DateField()
    #gender
    address= models.CharField(max_length=30)
    display_image = models.ImageField(upload_to="uploads", null="True") 
    #if in gender male then as default in avtar male pic otherwiser girl pic 
 