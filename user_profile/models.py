from django.db import models
from django.db.models import Sum
from datetime import datetime

class Category(models.Model):
    category = models.CharField(max_length=50)
    essential = models.BooleanField(default=False)
    planning_cost = models.FloatField(default=0)

    def total_spend(self):
        from bank_statement.models import BankStatement
        bank_statement = BankStatement.objects.filter(category__id=self.id).filter(
                         date__month=datetime.now().month).filter(kind='O')

        total_spend = bank_statement.aggregate(total = Sum('value'))['total']
        return total_spend if total_spend else 0

    def percentage_total_spend(self):
        return int((self.total_spend() * 100) / self.planning_cost)

    def __str__(self):
        return self.category

class Account(models.Model):
    bank_choices = (
        ('NU', 'Nubank'),
        ('CE', 'Caixa Econômica'),
        ('BR', 'Bradesco'),
        ('SAN', 'Santander'),
    )

    person_type_choices = (
        ('PF', 'Pessoa física'),
        ('PJ', 'Pessoa Jurídica')
    )

    nickname = models.CharField(max_length=100)
    bank = models.CharField(max_length=3, choices=bank_choices)
    person_type = models.CharField(max_length=2, choices=person_type_choices)
    value = models.FloatField()
    icon = models.ImageField(upload_to="icons")

    def __str__(self):
        return self.nickname

