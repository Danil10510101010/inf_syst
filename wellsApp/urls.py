from django.urls import path

from . import views

urlpatterns = [
    path("", views.charts, name="charts"),
    path("<int:well_id>/", views.wellDetails, name="details"),
]
