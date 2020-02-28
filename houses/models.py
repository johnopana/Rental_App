from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField()
    email =models.EmailField(blank=True)
    profile_pic= models.ImageField(upload_to='images/',default='images/avatar.png', blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        return cls.objects.all()    

    def __str__(self):
        return f'{self.name}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class House(models.Model):
    house_no = models.CharField(max_length=50)
    registry_no = models.CharField(max_length=100)
    house_location = models.CharField(max_length=50)
    house_pic = models.ImageField(upload_to='media/')
    house_type = models.CharField(max_length=100)
    no_of_rooms = models.CharField(max_length=5)

    price = models.CharField(max_length=100, default=0)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)


    def save_house(self):
        self.save()

    def delete_house(self):
        self.delete()

    @classmethod
    def search(cls,searchterm):
        search = cls.objects.filter(house_location__icontains=searchterm)
        return search

    @classmethod
    def find_house(cls,house_id):
        house= cls.objects.get(id=house_id)
        return house

    @classmethod
    def update_house(cls,id,house_type):
        cls.objects.filter(pk = id).update(house_type=house_type)
        new_name_object = cls.objects.get(house_type = house_type)
        new_name = new_name_object.house_type
        return new_name

    def __str__(self):
        return f'{self.house_no}'

    class Meta:
        ordering = ['-date_posted']

class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.PositiveIntegerField()
    owner_pic = models.ImageField(upload_to='images/', default='images/avatar.png')

    def save_owner(self):
        self.save()

    def delete_owner(self):
        self.delete()
    def __str__(self):
        return f'{self.first_name}'
