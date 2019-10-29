from django.contrib import admin
from app.models import Area
from app.models import Trench
from app.models import Building

class AreaAdmin(admin.ModelAdmin):
    pass

class TrenchAdmin(admin.ModelAdmin):
    pass

class BuildingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Area, AreaAdmin)
admin.site.register(Trench, TrenchAdmin)
admin.site.register(Building, BuildingAdmin)
