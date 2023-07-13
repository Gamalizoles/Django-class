"""
URL configuration for MorningDjangoHTMLFormsProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name= 'home-page'),
    path('add-product/', views.add_products, name= 'add-product-page'),
    path('products/', views.products, name= 'products-page'),
    path('delete-product/<id>', views.delete_product, name= 'del-pr'),
    path('update-product/<id>', views.update_product, name= 'upd-product')
]
