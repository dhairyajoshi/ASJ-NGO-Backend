from django.db import models
from core.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.
def  upload_to_opfp(instance,filename):
    return 'opfps/{filename}'.format(filename=filename)

class Organisation(models.Model):
    name = models.CharField(max_length=250)
    owner= models.OneToOneField(User, on_delete=models.CASCADE)
    members= models.ManyToManyField(User,related_name="member_list")
    address= models.TextField()
    details= models.TextField(default="")
    unique_id= models.CharField(max_length=250,unique=True)
    gallery= models.ManyToManyField('OrgGallery',related_name='org_gallery')
    pfp= models.ImageField(_("Image"),upload_to=upload_to_opfp,default='pfps/default.png')


class OrgGallery(models.Model):
    Image= models.ImageField()
    Organisation= models.ForeignKey(Organisation,on_delete=models.CASCADE,blank=True,null=True)
    Upload_date= models.DateField()


class Donation(models.Model):
    organisation= models.ForeignKey(Organisation,on_delete=models.CASCADE)
    sender= models.ForeignKey(User,on_delete=models.CASCADE)
    request= models.TextField()

