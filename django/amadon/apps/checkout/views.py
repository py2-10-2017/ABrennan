from django.shortcuts import render, redirect

def index(request):

    return redirect('/amadon')

def products(request):

    products = [
        { 'name': 'Openfan', 'price': 5.99 },
        { 'name': 'Flexsoft', 'price': 12.99 },
        { 'name': 'Rehome', 'price': 3.16 },
        { 'name': 'Vollux', 'price': 4.00 },
        { 'name': 'Inch Antam', 'price': 16.27 },
        { 'name': 'Unanamsoft', 'price': 5.99 },
        { 'name': 'Tam-Lex', 'price': 2.79 },
        { 'name': 'Konkin', 'price': 3.31 },
        { 'name': 'Silver Zamtech', 'price': 7.98 },
        { 'name': 'Mathtrax', 'price': 2.99 }
    ]

    products = { 'products': products }

    # saving products as variable to use when multiplying in buying process - normally would be database
    request.session['products'] = products

    return render(request, 'checkout/index.html', products)


def buy(request):

    try:
        request.session['newPurchases']
    except KeyError:
        request.session['newPurchases'] = []

    temp = request.session['newPurchases']
    temp.append(request.POST)
    request.session['purchases'] = temp

    p_id = int(request.POST['product_id'])-1
    price = request.session['products'][request.session['products'].keys()[0]][p_id]
    price = price['price']

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
    del request.session['num']

    return redirect('/amadon/checkout')
