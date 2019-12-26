from django.contrib import admin
from excavation.models import Area
from excavation.models import Trench
from excavation.models import Building
from excavation.models import Find
from excavation.models import Finding


class AreaAdmin(admin.ModelAdmin):
    search_fields = ['name', ]


class TrenchAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'area', 'editor', ]
    list_filter = ['area', 'editor', ]
    search_fields = ['name', ]


class BuildingAdmin(admin.ModelAdmin):
    autocomplete_fields = ['area', ]


class FindAdmin(admin.ModelAdmin):
    pass


class FindingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Area, AreaAdmin)
admin.site.register(Trench, TrenchAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Find, FindAdmin)
admin.site.register(Finding, FindingAdmin)
