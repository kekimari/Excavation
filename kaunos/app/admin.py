from django.contrib import admin
from app.models import Area
from app.models import Trench

class AreaAdmin(admin.ModelAdmin):
    pass

class TrenchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Area, AreaAdmin)
admin.site.register(Trench, TrenchAdmin)
