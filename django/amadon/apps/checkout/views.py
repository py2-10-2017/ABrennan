from django.shortcuts import render, redirect
from products import items

def index(request):

    return redirect('/amadon')

def products(request):

    context = {
        'items': items
    }

    return render(request, 'checkout/index.html', context)


def buy(request):

    try:
        request.session['newPurchases']
    except KeyError:
        request.session['newPurchases'] = []

    temp = request.session['newPurchases']
    temp.append(request.POST)
    request.session['purchases'] = temp

    p_id = int(request.POST['product_id'])-1
    price = items[p_id]['price']

    try:
        request.session['total']
    except KeyError:
        request.session['total'] = 0
        request.session['num'] = 0

    request.session['amount'] = price * int(request.POST['qty'])
    request.session['total'] += request.session['amount']
    request.session['num'] += int(request.POST['qty'])

    return redirect('/amadon/checkout')


def checkout(request):

    return render(request, 'checkout/checkout.html')


def empty(request):

    del request.session['purchases']
    del request.session['newPurchases']
    del request.session['total']
    #del request.session['num']

    return redirect('/amadon/checkout')
