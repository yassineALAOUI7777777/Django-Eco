from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products

from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    # categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)

#*******************scraping************


# import requests
# from bs4 import BeautifulSoup
# from django.shortcuts import render
# import unicodedata


# def get_Products(page):
#     src = page.content
#     soup = BeautifulSoup(src, "lxml")
#     prod=soup.find("div",{"class":"-paxs row _no-g _4cl-3cm-shs"})
#     products_name = prod.find_all("h3")
#     products_price = prod.find_all("div",{"class":"prc"})
#     # products_category = prod.find_all("p")
#     # products_des= prod.find_all("p")
#     # products_img = prod.find_all("img", {"decoding": "async"})

#     for i in range(len(products_name)):
#         name = products_name[i].text
#         # Check if a Recette object with the same title already exists in the database
#         if Products.objects.filter(name=name).exists():
#             continue
#         product = Products(
#               name = name,
#               price= products_price[i],
#             #   category= products_category[i].text,
#             #   description= products_des[i].text,
#             #   image= products_img[i].get("src"),

            
#         )
#         product.save()

# page = requests.get("https://www.jumia.ma/fashion-mode/")
# get_Products(page)

# def product_view(request):
    
#     product = Products.objects.all()

#     context = {
#         'products': product
#     }

#     return render(request, 'index.html', context)


