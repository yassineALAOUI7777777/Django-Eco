from .models import Products
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import Products
def scrape_and_save(request):
    # Replace this URL with the one you want to scrape
    url = "https://www.jumia.ma/fashion-mode/"
    page = requests.get(url)
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    prod = soup.find("div", {"class": "-paxs row _no-g _4cl-3cm-shs"})
    products_name = prod.find_all("h3")
    products_price = prod.find_all("div", {"class": "prc"})
    
    products_img = prod.find_all("img", {"class": "img"})
    

    for i in range(len(products_name)):
        name = products_name[i].text.strip()
        # Check if a Products object with the same name already exists in the database
        if Products.objects.filter(name=name).exists():
            continue
        price = int(''.join(filter(str.isdigit, products_price[i].text.strip())))
        
        image_url= products_img[i].get("data-src"),
        image_url = str(image_url).replace("',", "")[2:-1]
        print( image_url)
        product = Products(name=name, price=price,image=image_url)
        
        
        product.save()
    
    products = Products.objects.all()

    context = {
        'products': products
    }
    return render(request, "index.html", context)

