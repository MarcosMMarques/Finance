from django.shortcuts import render, redirect
from user_profile.models import Account, Category
from django.http import HttpResponse
from .models import BankStatement
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime, timedelta

def new_value(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        accounts = Account.objects.all()
        return render(request, 'new_value.html', {'categorys' : categorys, 'accounts' : accounts})
    
    elif request.method == 'POST':
        value = request.POST.get('value')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        date = request.POST.get('date')
        account_id = request.POST.get('account')
        account = Account.objects.get(id=account_id)
        kind = request.POST.get('kind')

        bank_statement = BankStatement(
           value=value, category_id=category_id, description=description,
           date=date, account=account, kind=kind 
        )

        bank_statement.save()
        
        if kind == 'I':
            account.value += float(value)
            messages.add_message(request, constants.SUCCESS, 'Entrada cadastrada com sucesso')
        else:
            account.value -= float(value)
            messages.add_message(request, constants.SUCCESS, 'Saida cadastrada com sucesso')
        
        account.save()
        return redirect('/statement/new_value/') 

def view_extract(request):
    accounts = Account.objects.all()
    categorys = Category.objects.all()

    account_get = request.GET.get('account')
    category_get = request.GET.get('category')

    bank_statements = BankStatement.objects.all()
    clear_filters = request.GET.get('clear_filters')
    period = request.GET.get('period')

    if clear_filters:
        return redirect('/statement/view_extract/')

    if account_get:
        bank_statements = bank_statements.filter(account__id=account_get)
    
    if category_get:
        bank_statements = bank_statements.filter(category__id=category_get)

    if period:
        now = datetime.now()
        if period == 'W':
            last_week = now - timedelta(days=7)
            bank_statements = bank_statements.filter(date__gte=last_week)
        elif period == 'M':
            last_month = now - timedelta(days=30)
            bank_statements = bank_statements.filter(date__gte=last_month)
        elif period == 'Y':
            last_year = now - timedelta(days=365)
            bank_statements = bank_statements.filter(date__gte=last_year)

    return render(request, 'view_extract.html', {
                                                    'accounts' : accounts, 'categorys' : categorys,
                                                    'bank_statements' : bank_statements.order_by('-date')
                                                }
    )
