from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name='homepage'),
  path('insertdata/', views.insertdata, name='insertdata'),
  path('viewdata/', views.viewdetails, name='viewdata'),
  path('details/<id>/', views.get_customer, name='get_customers'),
  path('delete/<id>/', views.deleteReq, name='delete'),
  path('update/<id>/', views.UpdateReq, name='update'),

  path('sendInfo/', views.sendInfo, name='sendInfo'),

  path('viewInfo/', views.viewInfo, name='viewInfo'),
  path('getInfo/<id>/', views.getInfo, name='get_info'),

  path('updateInfo/<id>/', views.updateInfo, name='update_info'),
  path('deleteInfo/<id>/', views.deleteInfo, name='delete_info'),
]