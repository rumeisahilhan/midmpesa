from __future__ import unicode_literals

import requests
from django.http import HttpResponse, JsonResponse
from django_daraja.mpesa.core import MpesaClient
from django.shortcuts import render

cl = MpesaClient()
stk_push_callback_url = 'https://api.darajambili.com/expess-payment'
b2c_callback_url = 'https://api.darajamnili.com/b2c/result'


def ouath_success(request):
    r = cl.access_token()
    return JsonResponse(r, safe=False)


def index(request):
    if request.method == "post":
        phone_number = request.post.get = ('phone')
        amount = request.POST.get('amount')
        amount = int(amount)
        account_refeence = 'rahma'
        transaction_desc = 'STK push Description'
        callback_url = stk_push_callback_url
        r = cl.stk_push(phone_number, amount, account_refeence, transaction_desc, callback_url)
        return JsonResponse(r.Response_description, safe=False)
    return render(request, 'index.html')
