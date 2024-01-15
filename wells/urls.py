from django.contrib import admin
from django.urls import include, path

from wellsApp import views

urlpatterns = [
    path("", views.charts, name="charts"),
    path("<int:well_id>/", views.wellDetails, name="details"),
    # path("wellsApp/", include("wellsApp.urls")),
    path("admin/", admin.site.urls),
]
