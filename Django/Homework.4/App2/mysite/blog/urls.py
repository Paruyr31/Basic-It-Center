from . import views
from django.urls import path

app_name = "blog"
urlpatterns = [
    path('product/<str:slug>/', views.product_detail, name="product_detail"),
    path('', views.ProductListView.as_view(), name='product_list')
]