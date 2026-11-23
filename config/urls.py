
from django.contrib import admin
from django.urls import path
from properties import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # DreamHomes homepage
    path("", views.home, name="home"),

    # Property details
    path(
        "property/<int:property_id>/",
        views.property_detail,
        name="property_detail"
    ),
]