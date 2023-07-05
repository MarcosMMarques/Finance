from django.db import models
from user_profile.models import Account, Category
import datetime

class BankStatement(models.Model):
    kind_choices = (
        ('I', 'Input'),
        ('O', 'Output')
    )

    value = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()
    date = models.DateField()
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    kind = models.CharField(max_length=1, choices=kind_choices)

    def __str__(self):
        return self.description