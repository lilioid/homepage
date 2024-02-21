from django.urls import path

from homepage.core import views

urlpatterns = [
    path("robots.txt", views.RobotsView.as_view(), name="robots.txt"),
    path("", views.HomeView.as_view(), name="index"),
    path("projects", views.ProjectsView.as_view(), name="projects"),
]
