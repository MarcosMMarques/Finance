from django.urls import path
from . import views

urlpatterns = [
    path('define_planning/', views.define_planning, name="define_planning"),
    path('update_planning_cost/<int:id>', views.update_planning_cost, name="update_planning_cost"),
    path('view_planning/', views.view_planning, name="view_planning"),
]