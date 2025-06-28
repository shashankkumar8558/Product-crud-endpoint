from django.urls import path
from myapp.views import home,ProductsList


urlpatterns = [
    path('',home),
    path('categories',ProductsList.as_view())
]