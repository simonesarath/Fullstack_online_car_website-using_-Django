from django.contrib import admin
from futurcars.models import Car,Booking,Contact

# Register your models here.
admin.site.register(Contact)
admin.site.register(Car)
admin.site.register(Booking)