from django.contrib import admin
from app.models import Area
from app.models import Trench
from app.models import Building
from app.models import Find
from app.models import Finding

class AreaAdmin(admin.ModelAdmin):
    search_fields = ['name',]

class TrenchAdmin(admin.ModelAdmin):
    pass

class BuildingAdmin(admin.ModelAdmin):
    autocomplete_fields = ['area',]

class FindAdmin(admin.ModelAdmin):
    pass

class FindingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Area, AreaAdmin)
admin.site.register(Trench, TrenchAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Find, FindAdmin)
admin.site.register(Finding, FindingAdmin)