# -*- coding: utf-8 -*-
from django import forms
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from registration.forms import RegistrationForm
from registration.signals import user_registered
from simple_classroom.apps.classroom.models import StudentProfile


class StudentRegistrationForm(RegistrationForm):
    first_name = forms.CharField(label=_(u'Nombre/s'))
    last_name = forms.CharField(label=_(u'Apellido'))
    cx = forms.CharField(label=_(u'CX'))
    telephone = forms.CharField(label=_(u'Teléfono'))


@receiver(user_registered)
def save_student_profile(sender, **kwargs):
    user = kwargs.get('user', None)
    if user:
        try:
            user.first_name = kwargs.get('request').POST.get('first_name')
            user.last_name = kwargs.get('request').POST.get('last_name')
            user.save()
            StudentProfile.objects.create(
                user=user,
                telephone=kwargs.get('request').POST.get('telephone'),
                cx=kwargs.get('request').POST.get('cx'))
        except:
            pass  # TODO: log me!!