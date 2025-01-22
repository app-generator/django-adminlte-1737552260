# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Project(models.Model):

    #__Project_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Project_FIELDS__END

    class Meta:
        verbose_name        = _("Project")
        verbose_name_plural = _("Project")


class Logfile(models.Model):

    #__Logfile_FIELDS__
    file_name = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    uploaded_at = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Logfile_FIELDS__END

    class Meta:
        verbose_name        = _("Logfile")
        verbose_name_plural = _("Logfile")


class Alert(models.Model):

    #__Alert_FIELDS__
    alert_code = models.IntegerField(null=True, blank=True)
    log_file = models.ForeignKey(logfile, on_delete=models.CASCADE)

    #__Alert_FIELDS__END

    class Meta:
        verbose_name        = _("Alert")
        verbose_name_plural = _("Alert")



#__MODELS__END
