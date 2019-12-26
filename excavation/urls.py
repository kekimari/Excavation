from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('finds/', views.FindListView.as_view(), name='finds'),
    path('findings/', views.FindingListView.as_view(), name='findings'),
    path('buildings/', views.BuildingListView.as_view(), name='buildings'),
    path('trenches/', views.TrenchListView.as_view(), name='trenches'),
    path('areas/', views.TrenchListView.as_view(), name='areas')
]
