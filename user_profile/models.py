from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=50)
    essential = models.BooleanField(default=False)
    planning_cost = models.FloatField(default=0)

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

