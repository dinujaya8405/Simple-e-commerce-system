from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import SuperCategory
from .models import Category
from .models import Color
from .models import Order
from .models import Cart
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse


def home(request):
    try:
        products = Product.objects.all()
        superCategory = SuperCategory.objects.all()
        category = Category.objects.all()
        n = len(products)

        categorizedList = []
        superList = []
        catList = []
        catWiseSuper = []
        for j in range(len(superCategory)):
            superList.append(str(superCategory[j].superCategory_name))
            categorizedList.append((str(superCategory[j].superCategory_name), []))

        for j in range(len(category)):
            name = category[j].category_name
            catList.append(name)
            name = category[j].superCategory_name
            catWiseSuper.append(name)

        for j in range(n):
            catName = products[j].product_category
            i = catList.index(str(catName))
            i = superList.index(str(catWiseSuper[i]))
            categorizedList[i][1].append(products[j])

        for j in range(len(categorizedList)):
            x = len(categorizedList[j][1])
            if x % 3 == 0:
                x = x//3
            else:
                x = (x//3)+1
            categorizedList[j] += ((range(1, x)),)
        j = int(0)
        while j < (len(categorizedList)):
            if len(categorizedList[j][1]) == 0:
                categorizedList.pop(j)
            else:
                j += 1

        params = {'superCategory':superCategory,'superList': superList, 'jrange': range(int(0), int(
            len(superCategory))), 'product_len': n, 'product': categorizedList}
        return render(request, 'shop/home.html', params)
    except:
        return render(request, 'shop/error.html',params)


def about(request):
    superCategory = SuperCategory.objects.all()
    params = {'superCategory': superCategory}
    return render(request, 'shop/about.html',params)


def contact(request):
    superCategory = SuperCategory.objects.all()
    params={'superCategory':superCategory}
    return render(request, 'shop/contact.html',params)


def productView(request):
    try:
        a = int(request.GET.get('val'))
        product = Product.objects.all()
        superCategory = SuperCategory.objects.all()

        for i in range(len(product)):
            if int(product[i].id) == a:
                prams = {'superCategory': superCategory,'product': product[i]}
                return render(request, "shop/productView.html", prams)
    except:
        superCategory = SuperCategory.objects.all()
        params={'superCategory':superCategory}
        return render(request,"shop/error.html",params)


def supercategory(request):
    try:
        superCat = request.GET.get('val')
        category = Category.objects.all()
        product = Product.objects.all()
        superCategory = SuperCategory.objects.all()
        n = len(product)
        categorizedList = []
        catList = []

        for i in range(len(category)):
            if str(category[i].superCategory_name) == str(superCat):
                catList.append(str(category[i].category_name))
                categorizedList.append((str(category[i].category_name), []))

        for j in range(n):
            catName = str(product[j].product_category)
        # print(catName,catList)
            if str(catName) in catList:
                i = catList.index(str(catName))
                categorizedList[i][1].append(product[j])

        for j in range(len(categorizedList)):
            x = len(categorizedList[j][1])
            if x % 3 == 0:
                x = x // 3
            else:
                x = (x // 3) + 1
            categorizedList[j] += ((range(1, x)),)
        j = int(0)
        while j < (len(categorizedList)):
            if len(categorizedList[j][1]) == 0:
                categorizedList.pop(j)
            else:
                j += 1
        empty=int(0)
        if len(categorizedList)==0:
            empty=int(1)
        print(superCat,empty)
        params = {'empty':empty,'superCategory': superCategory, 'jrange': range(int(0), int(len(catList))),
                  'product': categorizedList, 'Name': superCat}

        return render(request, 'shop/supercategory.html', params)
    except:
        superCategory = SuperCategory.objects.all()
        params={'superCategory':superCategory}
        return render(request,"shop/error.html",params)


def search(request):
    try:
        superCategory=SuperCategory.objects.all()
        search_key=request.POST
        search_key = search_key.get('search_key', False)
        product = Product.objects.all()
        search_key=list(search_key.split())
        data=[]
        for i in product:
            name=str(i.product_name)
            for j in search_key:
                if j.lower() in str(name).lower():
                    data.append(i)
                    break
        empty=int(0)
        if len(data)==0:
            empty=int(1)
        params={'data':data,'empty':empty,'superCategory':superCategory}
        return render(request,"shop/search.html",params)
    except:
        superCategory = SuperCategory.objects.all()
        params = {'superCategory': superCategory}
        return render(request, "shop/error.html", params)

def category(request):
    try:
        superCategory=SuperCategory.objects.all()
        category = request.GET.get('val')
        product = Product.objects.all()
        data=[]
        for i in product:
            name=str(i.product_category)
            if name==str(category):
                data.append(i)
        empty=int(0)
        if len(data)==0:
            empty=int(1)
        params={'data':data,'empty':empty,'superCategory':superCategory,'category':category}
        return render(request,"shop/category.html",params)
    except:
        superCategory = SuperCategory.objects.all()
        params = {'superCategory': superCategory}
        return render(request, "shop/error.html", params)


def error(request):
    superCategory = SuperCategory.objects.all()
    params = {'superCategory': superCategory}
    return render(request, "shop/error.html",params)


def addcart(request):
    try:
        a = request.GET.get('val')
        product = Product.objects.all()
        superCategory = SuperCategory.objects.all()
        for i in range(len(product)):
            if int(product[i].id) == int(a):
                params = {'superCategory': superCategory,"prod": product[i]}
                return render(request, "shop/addcart.html", params)
        return render(request, "shop/error.html")
    except:
        superCategory = SuperCategory.objects.all()
        params = {'superCategory': superCategory}
        return render(request,"shop/error.html",params)


def checkout(request):
    return HttpResponse("checkout")

def confirmBuying(request):
    try:
        superCategory = SuperCategory.objects.all()
        prod_id = request.POST['prod_id']
        prod_quantity=request.POST['prod_quantity']
        cart_instance= Cart.objects.create(user=request.user,product_id=prod_id,product_quantity=prod_quantity,order_status='Not Ordered')
        print("okk")
        params={'superCategory': superCategory}
        return HttpResponseRedirect('confirmOrder')
    except:
        superCategory = SuperCategory.objects.all()
        params = {'superCategory': superCategory}
        return render(request,"shop/error.html",params)
    

def confirmOrder(request):
    if 1:
        superCategory = SuperCategory.objects.all()
        product = Product.objects.all()
        cart = Cart.objects.all()
        forOrder = []
        cost=int(0)

        for prod in cart:
            if prod.user == request.user and prod.order_status == 'Not Ordered':
                for mainProd in product:
                    if mainProd.pk==prod.product_id:
                        forOrder.append((prod,mainProd,prod.product_quantity*mainProd.product_price))
                        cost+=int(prod.product_quantity)*int(mainProd.product_price)
        params = {'superCategory':superCategory,'forOrder':forOrder,'cost':cost}
        return render(request,"shop/confirmOrder.html",params)
    


def confirmation(request):
    superCategory = SuperCategory.objects.all()

    receiver_name=request.POST['receiver_name']
    receiver_email=request.POST['receiver_email']
    receiver_mobile=request.POST['receiver_mobile']
    receiver_address=request.POST['receiver_address']
    total_price=int(request.POST['total_price'])

    order_instance=Order.objects.create(user=request.user,receiver_name=receiver_name,receiver_email=receiver_email,receiver_mobile=receiver_mobile,receiver_address=receiver_address,total_price=total_price,service_charge=int(0),total_bill=total_price,payment_status='Not Paid',shipping_status='Not Shipped')
    product = Product.objects.all()
    cart = Cart.objects.all()
    for prod in cart:
            if prod.user == request.user and prod.order_status == 'Not Ordered':
                for mainProd in product:
                    if mainProd.pk==prod.product_id:
                        cart_instance=Cart.objects.get(product_id=prod.product_id)
                        cart_instance.order_status='Ordered'
                        cart_instance.save()
    params = {'superCategory': superCategory}
    return render(request,"shop/confirmation.html",params)