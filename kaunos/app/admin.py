from django.contrib import admin
from app.models import Area

class AreaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Area, AreaAdmin)
