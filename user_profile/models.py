from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

def user_directory_path(instance, filename):
    return 'quicktutorsApp/media/user_directory/user_{0}/{1}'.format(instance.user.id, filename)

def reunionSite_directory_path(self,filename):
    return 'quicktutorsApp/media/reunion_site_directory/{0}'.format(filename)

def university_directory_path(self,filename):
    return 'quicktutorsApp/media/university_directory/{0}'.format(filename)

class Area(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Career(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class ReunionSite(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to=reunionSite_directory_path, default='reunion_site_directory/no-image.jpg')
    address = models.TextField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to=university_directory_path, default='university_directory/no-img.jpg')
    reunion_sites = models.ManyToManyField(ReunionSite, default='')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    area = models.ForeignKey(Area, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    isTutor = models.BooleanField(default=False)
    bio = models.TextField(max_length=300, null=True, blank=True)
    studentID = models.CharField(max_length=10)
    picture = models.ImageField(upload_to=user_directory_path, default='quicktutorsApp/media/user-character.png')
    career = models.ForeignKey(Career, null=True)
    university = models.ForeignKey(University, null=True)
    subjects = models.ManyToManyField(Subject)
    video = models.URLField(null=True, blank=True)
    begin_time = models.TimeField(blank=True, null=True, default=timezone.now)
    end_time = models.TimeField(blank=True, null=True, default=timezone.now)
    quickfirequestions_available = models.IntegerField(default=0)

    def __unicode__(self):
        if self.user:
            return self.user.username
        return ''

    def __str__(self):
        if self.user:
            return self.user.username
        return ''

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, new = UserProfile.objects.get_or_create(user=instance)

