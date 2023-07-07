from django.shortcuts import render, redirect
from user_profile.models import Category
from .models import Bill, BillPaid
from django.contrib import messages
from django.contrib.messages import constants
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta

def define_bill(request):
    if request.method == "GET":
        categorys = Category.objects.all()
        return render(request, 'define_bill.html', {'categorys': categorys})
    else:
        title = request.POST.get('title')
        value = request.POST.get('value')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        category = request.POST.get('category')
        bill = Bill(title=title, 
                    value=value, 
                    description=description, 
                    due_date=due_date, 
                    category_id=category)
        bill.save()

        messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso')
        return redirect('/bill/define_bill/')

def view_bills(request):
    bills = Bill.objects.all()
    bills_paid = BillPaid.objects.all().values('bill')

    bills_passed_due_date = bills.filter(due_date__lt=datetime.now()).exclude(id__in=bills_paid)
    bills_approaching_due_date = bills.filter(due_date__lte = datetime.now() + timedelta(7)).filter(due_date__gte=datetime.now()).exclude(id__in=bills_paid)
    remaining_bills = bills.exclude(id__in=bills_approaching_due_date).exclude(id__in=bills_paid).exclude(id__in=bills_passed_due_date)

    return render(request, 'view_bills.html', {'bills_passed_due_date' : bills_passed_due_date,
                                               'bills_approaching_due_date' : bills_approaching_due_date,
                                                'remaining_bills' : remaining_bills,
                                              })

@csrf_exempt
def pay_bill(request, id):
    print(id)
    bill = Bill.objects.get(id=id)
    bill_paid = BillPaid(payment_date=datetime.now(), bill=bill)
    bill_paid.save()
    
    messages.add_message(request, constants.SUCCESS, 'Conta paga com sucesso')
    return redirect('/bill/view_bills/')