from django.contrib import admin
from .models import Hospital, OxygenSupplier, Med

# Register your models here.

admin.site.register(Hospital)
admin.site.register(OxygenSupplier)
admin.site.register(Med)
