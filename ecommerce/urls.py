"""
URL configuration for ecommerce project.

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
# from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static



#backend

from backend.views import dashboard
from backend.views import register
from backend.views import login
from backend.views import logout
from backend.views import update
from backend.views import delete
from backend.views import viewdata
from backend.views import addcategory
from backend.views import viewcategory
from backend.views import deletecategory
from backend.views import updatecategory
from backend.views import change
from backend.views import addsubcate
from backend.views import viewsubcate
from backend.views import deletesubcate
from backend.views import updatesubcate
from backend.views import addproduct
from backend.views import viewproduct
from backend.views import deleteproduct
from backend.views import updateproduct
from backend.views import pchange

#frontend

from firstapp.views import home
from firstapp.views import fashion
from firstapp.views import jewellery
from firstapp.views import electronic


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #backend

    path('dashboard/',dashboard),
    path('register/',register),
    path('login/',login),
    path('logout/',logout),
    path('update/<int:id>/',update),
    path('delete/<int:id>/',delete),
    path('viewdata/',viewdata),
    path('addcategory/',addcategory),
    path('viewcategory/',viewcategory),
    path('delete/<int:id>',deletecategory),
    path('update/<int:id>',updatecategory),
    path('changestatus/<int:id>',change),
    path('addsubcate/',addsubcate),
    path('viewsubcate/',viewsubcate),
    path('deletesub/<int:id>',deletesubcate),
    path('updatesub/<int:id>',updatesubcate),
    path('addproduct/',addproduct),
    path('viewproduct/',viewproduct),
    path('updateproduct/<int:id>',updateproduct),
    path('deleteproduct/<int:id>',deleteproduct),
    path('pchange/<int:id>',pchange),
    
    #frontend
    path('',home),
    path('fashion/',fashion),
    path('jewellery/',jewellery),
    path('electronic/',electronic),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
