from django.shortcuts import render, redirect
from user_profile.models import Category
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.messages import constants

def define_planning(request):
    categorys = Category.objects.all()
    return render(request, 'define_planning.html', {'categorys' : categorys})

@csrf_exempt
def update_planning_cost(request, id):
    new_value = json.load(request)['new_value']
    category = Category.objects.get(id=id)
    category.planning_cost = new_value
    try:
        category.save()
        messages.add_message(request, constants.SUCCESS, 'Valor atualizado com sucesso')
    except:
        messages.add_message(request, constants.ERROR, 'Erro ao atualizar o valor')

    return redirect('/planning/define_planning/')

def view_planning(request):
    categorys = Category.objects.all()
    return render(request, 'view_planning.html', {'categorys' : categorys})


