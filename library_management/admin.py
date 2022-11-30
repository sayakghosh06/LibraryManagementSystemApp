from django.contrib import admin

from library_management.models import Bookadd,Memberadd,Issuebook,Returnbook

# Register your models here.

admin.site.register(Bookadd)
admin.site.register(Memberadd)
admin.site.register(Issuebook)
admin.site.register(Returnbook)