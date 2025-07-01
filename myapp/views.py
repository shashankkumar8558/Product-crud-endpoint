from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse,JsonResponse
from django.views import View
from .models import Product
import json


def home(request):
  return HttpResponse(content="Thank you for using this API now you can go to /categories for further post and get products")

""" this view will filter out the products based on the params provided, it can handle upto 3 fields for now """
@method_decorator(csrf_exempt,name='dispatch')
class ProductsList(View):
  def get(self,request):
        try:
            categoryParam = request.GET.getlist('category');
            soldParam = request.GET.get('sold');
            titleParam = request.GET.get('title');
            min_price = request.GET.get('minPrice')
            max_price = request.GET.get('maxPrice')
            print(categoryParam,soldParam,titleParam,"lets see the structure of request in this ");
            
            """ accumulating all the params into a dictionary for passing it as a kwargs in filter() later. """
            
            filters = {}
            if len(categoryParam) > 0:
              filters['category__in'] = categoryParam;
            if soldParam is not None:
              filters['sold'] = soldParam;
            if titleParam:
              filters['title__icontains'] = titleParam;
            if min_price:
                try:
                    filters['price__gte'] = float(min_price)
                except ValueError:
                    return JsonResponse({"error": "minPrice must be a valid number"}, status=400)
            if max_price:
                try:
                    filters['price__lte'] = float(max_price)
                except ValueError:
                    return JsonResponse({"error": "maxPrice must be a valid number"}, status=400)
            
            print(filters,"lets see what's in Filters")
            fetchedProduct = Product.objects.filter(**filters);
            
            """ making an empty list first and after that appending  """
            output = [];
            for fp in fetchedProduct:
              output.append({
                "title" : fp.title,
                "price" : fp.price,
                "description" : fp.description,
                "category" : fp.category,
                "image" : fp.image,
                "sold" : fp.sold,
                "isSale" : fp.isSale,
                "dateOfSale" : fp.dateOfSale
              })
                
            return JsonResponse({"message" : "fetched successfully","products" : output},safe=False,status=200);
        except Exception as e:
          return JsonResponse({"error" : str(e)},status=400)
  
  
  def post(self, request):
        try:
            """ this line just decodes the raw data which is in bytes type into string and then json.loads convert that into python dict or python list depending upon the strucutre of the JSON string """
            
            data = json.loads(request.body.decode())
            
            """ so now data is a list of dict but .bulk_create() only accepts object of model so in that case we are converting it from the list of dict to list of model's object """
            
            product = [
                Product(
                    title=item["Title"],
                    price=item["Price"],
                    description=item["Description"],
                    category=item["Category"],
                    image=item["Image"],
                    sold=item["Sold"],
                    isSale=item["Is Sale"],
                    dateOfSale=item["DateOfSale"] or None
                )
                for item in data
            ]
            Product.objects.bulk_create(product)
            return JsonResponse({"message": "Products created successfully"}, status=201)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)