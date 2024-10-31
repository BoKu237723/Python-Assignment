from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/list/', permanent=False), name='home'),
    path('create/', views.add, name='create'),
    path('list/', views.list, name='list'),
    path('update/<int:student_id>/', views.update, name='update'),
    path('delete/<int:student_id>/', views.delete, name='delete'),
]
