from django.db import models
from user_profile.models import Category

class Bill(models.Model):

    value = models.FloatField(null=False)
    title = models.CharField(max_length=50, null=False)
    description = models.TextField()
    due_date = models.DateField(null=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=False)

    def __str__(self):
        return self.title        
    
class BillPaid(models.Model):
    bill =  models.ForeignKey(Bill, on_delete=models.DO_NOTHING)
    payment_date = models.DateField(null=False)    

