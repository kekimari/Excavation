from django.contrib import admin
from app.models import Area
from app.models import Trench
from app.models import Building
from app.models import Find

class AreaAdmin(admin.ModelAdmin):
    pass

class TrenchAdmin(admin.ModelAdmin):
    pass

class BuildingAdmin(admin.ModelAdmin):
    pass

class FindAdmin(admin.ModelAdmin):
    pass

admin.site.register(Area, AreaAdmin)
admin.site.register(Trench, TrenchAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Find, FindAdmin)