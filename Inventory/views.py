from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

# Create your views here.
class ProductsView(APIView):

    def get(self, request):
        all_products = Products.objects.all()

        product_data =[]

        for product in all_products:
            single_product={
                "product_id": product.id,
                "product_name": product.product_name,
                "product_code": product.product_code,
                "product_price": product.product_price
            }
            # print(single_product)
            product_data.append(single_product)

        return Response(product_data)


    def post(self,request):

        new_product = Products(product_name = request.data["product_name"],product_code = request.data["product_code"],product_price=request.data["product_price"])
        
        new_product.save()
        # print(request.data)

        return Response('Data Saved') 
    
class ProductsViewById(APIView):

    def get(self,request,id):       
        product = Products.objects.get(id = id)

        single_product={
            "product_id": product.id,
            "product_name": product.product_name,
            "product_code": product.product_code,
            "product_price": product.product_price
        }

        return Response(single_product)
    
    def patch(self,request,id):
        product = Products.objects.filter(id = id)

        product.update(product_name = request.data["product_name"], product_code = request.data["product_code"], product_price = request.data["product_price"])

        # print(request.data)
        return Response("Updated a data") 
    
    def delete(self,request,id):
        product = Products.objects.get(id = id)
        product.delete()

        return Response("Deleted a data")
