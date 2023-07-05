# Generated by Django 4.2.3 on 2023-07-03 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('essential', models.BooleanField(default=False)),
                ('planning_cost', models.FloatField(default=0)),
            ],
        ),
    ]