from json import JSONEncoder

from django.shortcuts import render
#import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
from web.models import User,Token, Expense, Income
# Create your views here.
@csrf_exempt
def submit_expense(request):
    print("Hello!! expense")
    #TODO: data might be validate
    print (request.POST)
    mytoken = request.POST['token']
    if 'token' in request.POST:
        mytoken = request.POST['token']
        text = request.POST['text']
        amount = request.POST['amount']

        if 'date' not in request.POST:
            date = datetime.datetime.now()
        else:
            date = request.POST['date']
        user= User.objects.filter(token__token=mytoken).get()
        Expense.objects.create(user=user, text=text, date=date, amount=amount)
        print(mytoken)


    return JsonResponse({

        'status': 'ok',
    }, encoder=JSONEncoder)


@csrf_exempt
def submit_income(request):
    print("Hello!! income")
    #TODO: data might be validate
    print (request.POST)
    mytoken = request.POST['token']
    if 'token' in request.POST:
        mytoken = request.POST['token']
        text = request.POST['text']
        amount = request.POST['amount']

        if 'date' not in request.POST:
            date = datetime.datetime.now()
        else:
            date = request.POST['date']
        user= User.objects.filter(token__token=mytoken).get()
        Income.objects.create(user=user, text=text, date=date, amount=amount)
        print(mytoken)


    return JsonResponse({

        'status': 'ok',
    }, encoder=JSONEncoder)