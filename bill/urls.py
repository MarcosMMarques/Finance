from django.urls import path
from . import views

urlpatterns = [
    path('define_bill/', views.define_bill, name="define_bill"),
    path('view_bills/', views.view_bills, name="view_bills"),
    path('pay_bill/<int:id>', views.pay_bill, name="pay_bill"),
]