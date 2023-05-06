from django.db import models

from decimal import Decimal
class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    #category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    image = models.CharField(max_length=2000)

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Products.objects.all()

    # @staticmethod
    # def get_all_products_by_categoryid(category_id):
    #     if category_id:
    #         return Products.objects.filter (category=category_id)
    #     else:
    #         return Products.get_all_products()