from django.shortcuts import render, redirect
from django.views import View
from .models import Product
from django.db.models import Q
from django.http import JsonResponse
from app.models import Customer, Cart
# Create your views here.
# --------------------------------------------------------------------------------------------------
def home(request):
    return render(request, 'app/home.html')

# --------------------------------------------------------------------------------------------------
def about(request):
    return render(request, 'app/about.html')

# --------------------------------------------------------------------------------------------------
def contact(request):
    return render(request, 'app/contact.html')

# --------------------------------------------------------------------------------------------------
class Categoryview(View): 
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title   = Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html",locals())


# --------------------------------------------------------------------------------------------------
class CategoryTitle(View): 
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title   = Product.objects.filter(title=val).values('title')
        return render(request, "app/category.html",locals())


# --------------------------------------------------------------------------------------------------
class Detailview(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render (request, 'app/detail.html', locals())


# --------------------------------------------------------------------------------------------------
def addcart(request):
    user = request.user 
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/mycart')
# --------------------------------------------------------------------------------------------------
def showmycart(request):
    user =request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
        totalamount = amount + 150
    return render (request, 'app/addcart.html',locals())

# --------------------------------------------------------------------------------------------------
class Checkout(View):
    def get(self,request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount = famount + 40
        return render (request, 'app/checkout.html',locals())


        



# --------------------------------------------------------------------------------------------------
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 150
        #print(prod_id)
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount,
        }
        return JsonResponse(data)
# --------------------------------------------------------------------------------------------------
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart = cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 150
        #print(prod_id)
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount,
        }
        return JsonResponse(data)
    
# --------------------------------------------------------------------------------------------------
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 150
        #print(prod_id)
        data={
            
            'amount':amount,
            'totalamount':totalamount,
        }
        return JsonResponse(data)