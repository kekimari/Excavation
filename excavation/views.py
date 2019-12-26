from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin

from excavation.models import Building, Find, Finding, Trench, Area


def index(request):
    num_finds = Find.objects.count()
    num_findings = Finding.objects.count()
    num_buildings = Building.objects.count()
    num_trenches = Trench.objects.count()

    context = {
        'num_finds': num_finds,
        'num_findings': num_findings,
        'num_buildings': num_buildings,
        'num_trenches': num_trenches,
    }
    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'excavation/about.html')


class FindListView(PermissionRequiredMixin, generic.ListView):
    model = Find
    permission_required = 'excavation.view_find'
    paginate_by = 10


class FindingListView(PermissionRequiredMixin, generic.ListView):
    model = Finding
    permission_required = 'excavation.view_finding'
    paginate_by = 10


class BuildingListView(PermissionRequiredMixin, generic.ListView):
    model = Building
    permission_required = 'excavation.view_building'
    paginate_by = 10


class TrenchListView(PermissionRequiredMixin, generic.ListView):
    model = Trench
    permission_required = 'excavation.view_trench'
    paginate_by = 10


class AreaListView(PermissionRequiredMixin, generic.ListView):
    model = Area
    permission_required = 'excavation.view_area'
    paginate_by = 10