from django.urls import path
from .views import ProjectDetailView

urlpatterns = [
    path('<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),
]
