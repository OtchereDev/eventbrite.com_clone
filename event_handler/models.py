from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin,
                                        BaseUserManager)

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.core.validators import MinValueValidator


today=timezone.now()

class CustomerPublisherManager(BaseUserManager):
    
    def create_superuser(self,email,user_name,
                        first_name,last_name,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError('super user must be assigned is_staff = True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('super user must be assigned is_superuser = True')

        return self.create_user(email,user_name,first_name,last_name,password,**other_fields)
    
    def create_user(self,email,user_name,
                        first_name,last_name,password,**other_fields):
        
        if not email:
            raise ValueError('You must provide an email')

        email=self.normalize_email(email)
        user=self.model(email=email,user_name=user_name,first_name=first_name,
                        last_name=last_name,**other_fields)
        user.set_password(password)
        user.save()
        return user


class Publisher(AbstractBaseUser,PermissionsMixin):
    
    email=models.EmailField(max_length=350,unique=True)
    user_name=models.CharField(max_length=250,unique=True)
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    company=models.CharField(blank=True,null=True,max_length=250)
    start_date=models.DateTimeField(default=timezone.now)
    about=models.TextField(blank=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    object=CustomerPublisherManager()


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['user_name','first_name','last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Event(models.Model):
    name=models.CharField(max_length=255)
    event_date= models.DateTimeField()
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    number_of_participant=models.PositiveIntegerField()
    fylier=models.ImageField(null=True,blank=True)
    enrolled_participant=models.ManyToManyField("Participant", 
                                    verbose_name=_("Participant that that have enrolled for the event "),blank=True)
    is_active=models.BooleanField(default=True)
    slug=models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        return super(Event, self).save(*args, **kwargs)

        
# future use
# ------------- 
# @receiver(pre_save, sender=Event)  
# def save_is_Active(sender, instance, **kwargs):
    
#     if today<instance.event_date:
#         instance.is_active=True
       
#     else:
#         instance.is_active=False
       

class Participant(models.Model):
    email=models.EmailField(max_length=350)
    full_name=models.CharField(max_length=255)
    event_reg= models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_no=models.PositiveIntegerField(validators=[MinValueValidator(1)])

