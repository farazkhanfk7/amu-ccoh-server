from django.contrib import admin
from .models import Hospital, OxygenSupplier, Med, Notice

# Register your models here.

admin.site.register(Hospital)
admin.site.register(OxygenSupplier)
admin.site.register(Med)
admin.site.register(Notice)
