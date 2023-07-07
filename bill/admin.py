from django.contrib import admin
from .models import Bill, BillPaid

admin.site.register(Bill)
admin.site.register(BillPaid)
    