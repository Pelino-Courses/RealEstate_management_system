from django.contrib import admin
from Property_app.models import Property,Lease,Units,Tenant
# Register your models here.

admin.site.register(Property)
admin.site.register(Lease)
admin.site.register(Units)
admin.site.register(Tenant)