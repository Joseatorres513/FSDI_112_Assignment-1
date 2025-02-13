
from django.urls import path
from posts import views


urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("new", views.CreateView.as_view(), name="new"),
]