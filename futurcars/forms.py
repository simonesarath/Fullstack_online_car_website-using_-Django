from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from futurcars.models import Booking, Car

class BookingForm(forms.ModelForm):
    car = forms.ModelChoiceField(queryset=Car.objects.all(), label ="Select Car")
    
    class Meta:
        model = Booking
        fields = "__all__"