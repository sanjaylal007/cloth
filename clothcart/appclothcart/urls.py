from . import views
from django.urls import path

app_name='appclothcart'

urlpatterns = [
    path('',views.cloths,name='cloths'),
    path('cloth/<int:cloth_id>/',views.detail,name='detail'),
    path('add/',views.addcloth,name='addcloth'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')

]