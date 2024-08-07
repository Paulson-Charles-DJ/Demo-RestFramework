from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class ProductsView(APIView):

    def get(self, request):
        all_products = Products.objects.all()

        serialized_productdata = Products_Serializer(all_products, many=True).data
        
        # product_data =[]
        # for product in all_products:
        #     single_product={
        #         "product_id": product.id,
        #         "product_name": product.product_name,
        #         "product_code": product.product_code,
        #         "product_price": product.product_price
        #     }
        #     product_data.append(single_product)

        return Response(serialized_productdata)


    def post(self,request):  

        # new_product = Products(product_name = request.data["product_name"],product_code = request.data["product_code"],product_price=request.data["product_price"])     

        new_product = Products_Serializer(data = request.data)
        
        if new_product.is_valid():
            new_product.save()
            return Response("Data Saved")
        else:
            return Response(new_product.errors)
        
        # return Response('Data Saved') 
    
class ProductsViewById(APIView):

    def get(self,request,id):       
        product = Products.objects.get(id = id)

        # single_product={
        #     "product_id": product.id,
        #     "product_name": product.product_name,
        #     "product_code": product.product_code,
        #     "product_price": product.product_price
        # }

        single_product= Products_Serializer1(product).data

        return Response(single_product)
    
    def patch(self,request,id):
        # product = Products.objects.filter(id = id)
        # product.update(product_name = request.data["product_name"], product_code = request.data["product_code"], product_price = request.data["product_price"])
        # print(request.data)

        product = Products.objects.get(id = id)
        product_update= Products_Serializer(product, data = request.data, partial=True)

        if product_update.is_valid():
            product_update.save()
             
        else:
            return Response(product_update.errors)
        return Response("Updated a data") 
    
    def delete(self,request,id):
        product = Products.objects.get(id = id)
        product.delete()

        return Response("Deleted a data")
