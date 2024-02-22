from django.urls import path

from homepage.blog import views

app_name = "homepage_blog"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<str:category>", views.CategoryIndexView.as_view(), name="category_index"),
    path("<str:category>/<str:post>", views.PostView.as_view(), name="post"),
]
