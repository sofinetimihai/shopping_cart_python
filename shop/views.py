from django.shortcuts import render
from shop.models import Product, Category

# Create your views here.


def home(request):
    return render(request, "shop/home.html", {'message': 'Hi, there! pam pam'})


def product_list(request):
    # Creating an entry
    # return render(request, "shop/home.html", {'message': 'asdasdasdsa da da'})

    obiecte = Product.objects.all()

    return render(request, "shop/list.html", {'products': obiecte})


def product_list_by_category(request, categoryid):

    lista_produse = Product.objects.filter(category_id=categoryid)

    lista_category = Category.objects.all()

    return render(request, "shop/list.html", {'products': lista_produse, 'category': lista_category })

def product_detail(request, id):

    produs = Product.objects.get(pk=int(id))

    return render(request, "shop/produs.html", {'produs': produs})


