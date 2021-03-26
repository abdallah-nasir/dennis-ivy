from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer=request.user.customer 
        order,created = Order.objects.get_or_create(customer=customer,complete=False) 
        items = order.orderitem_set.all()  #items attached to that order
    else: #this is when the user is not logged in 
        items = []
        order = {"get_total":0,"get_cart_total":0} 
    products=Product.objects.all()
    context={"products":products,"order":order}
    return render(request,"store/store.html",context)

def cart(request): 
    if request.user.is_authenticated:
        customer=request.user.customer 
        order,created = Order.objects.get_or_create(customer=customer,complete=False) 
        items = order.orderitem_set.all()  #items attached to that order
    else: #this is when the user is not logged in 
        items = ["get_cart_items"]
        order = ["order"]
    context={"items":items,"order":order}

    return render(request,"store/cart.html",context)

@csrf_exempt
def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer 
        order,created = Order.objects.get_or_create(customer=customer,complete=False) 
        items = order.orderitem_set.all()  #items attached to that order
    else: #this is when the user is not logged in 
        items = []
        order = {"get_total":0,"get_cart_total":0} 
    context={"items":items,"order":order}
    return render(request,"store/checkout.html",context)

def updateitem(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    print("Action:",action)
    print("ProductId:",productId)
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer,complete=False) 
    orderItem , created = OrderItem.objects.get_or_create(order=order,product=product)
    if action == 'add':
       orderItem.quantity = (orderItem.quantity + 1)

    elif action == 'remove':
	    orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
    	orderItem.delete()
    return JsonResponse("item was added",safe=False)


