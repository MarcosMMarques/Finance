from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Account, Category
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Sum
from django.core.files.uploadedfile import UploadedFile
import imghdr


def home(request):
    accounts = Account.objects.all()
    total_account = accounts.aggregate(Sum('value'))['value__sum']
    category_quantity = Category.objects.count()
    essential_category_percent = Category.objects.filter(essential=True).count() / category_quantity * 100
    not_essential_category_percent = Category.objects.filter(essential=False).count() / category_quantity * 100
    
    return render(request, 'home.html', 
                    {
                        'accounts': accounts, 'total_account': total_account, 
                        'essential_category_percent': int(essential_category_percent),
                        'not_essential_category_percent': int(not_essential_category_percent)
                    }
                )

def manage(request):
    accounts = Account.objects.all()
    categorys = Category.objects.all()
    total_account = accounts.aggregate(Sum('value'))['value__sum']
    bank_choices  = Account.bank_choices

    return render(request, 'manage.html', 
                  {'accounts' : accounts, 'total_account': total_account, 
                   'categorys': categorys, 'bank_choices': bank_choices}
                 )

def register_bank(request):
    nickname = request.POST.get('nickname')
    bank = request.POST.get('bank')
    person_type = request.POST.get('person_type')
    value = request.POST.get('value')
    icon = request.FILES.get('icon')
    image_extensions = ['jpg', 'jpeg', 'png', 'bmp']
    icon_extension = imghdr.what(icon)

    if( len(nickname.strip()) == 0 or len(value.strip()) == 0 
        or not isinstance(float(value), float) or not (icon_extension in image_extensions) 
    ):
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return redirect('/profile/manage/')

    account = Account(
        nickname=nickname,
        bank=bank,
        person_type=person_type,
        value=value,
        icon=icon
    )

    account.save()

    messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso')
    return redirect('/profile/manage/')

def delete_bank(request, id):
    account = Account.objects.get(id=id)
    account.delete()

    messages.add_message(request, constants.SUCCESS, 'Conta deletada com sucesso')
    return redirect('/profile/manage/')

def register_category(request):
    category = request.POST.get('category')
    essential = bool(request.POST.get('essential'))

    if len(category.strip()) == 0 or not isinstance(essential, bool):
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return redirect('/profile/manage/')

    category = Category( 
        category=category,
        essential=essential
    )

    category.save()

    messages.add_message(request, constants.SUCCESS, 'Categoria cadastrada com sucesso')
    return redirect('/profile/manage/')

def update_category(request, id):
    category = Category.objects.get(id=id)
    category.essential = not category.essential
    category.save()


    messages.add_message(request, constants.SUCCESS, 'Categoria atualizada com sucesso')
    return redirect('/profile/manage')