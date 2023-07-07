from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('manage/', views.manage, name='manage'),
    path('register_bank/', views.register_bank, name="register_bank"),
    path('delete_bank/<int:id>', views.delete_bank, name="delete_bank"),
    path('register_category/', views.register_category, name="register_category"),
    path('update_category/<int:id>', views.update_category, name="update_category"),
    path('dashboard/', views.dashboard, name="dashboard"),
]