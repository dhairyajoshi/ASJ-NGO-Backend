from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomAccountManager(BaseUserManager):
    
    def create_superuser(self, email, name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, name, password, **other_fields)

    def create_user(self, email, name, password, **other_fields):
        other_fields.setdefault('is_active', True)
        if not email:
            raise ValueError(_('You must provide an email'))

        user = self.model(email=email,
                          name=name, **other_fields)
        user.set_password(password)
        user.save()
        return user

def  upload_to_upfp(instance,filename):
    return 'upfps/{filename}'.format(filename=filename)

def  upload_to_aadhar(instance,filename):
    return 'aadhar/{filename}'.format(filename=filename)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=150, blank=True)
    username = None
    email = models.EmailField(_('email address'), unique=True)
    pfp= models.ImageField(_("Image"),upload_to=upload_to_upfp,default='pfps/default.png')
    bio= models.TextField(default="")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    aadhar= models.ImageField(_("Image"),upload_to=upload_to_aadhar,default='aadhar/default.png')
    dob= models.DateField(null=True,blank=True)
    address= models.TextField()
    city= models.CharField(max_length=150)
    state= models.CharField(max_length=150)
    pincode= models.IntegerField(null=True,blank=True)
    gallery = models.ManyToManyField('UserGallery',related_name="user_gallery")
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    

    def __str__(self): 
        return self.email

class UserGallery(models.Model):
    image= models.ImageField()
    user= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    Upload_date= models.DateField()

    def __str__(self):
        return self.user

