from django.urls import path 
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('user/', views.UserList.as_view(), name='user_list'),
    path('user/<int:pk>', views.UserDetail.as_view(), name='user_detail'),

    path('category/', views.CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name='category_detail'),

    path('activity/', views.ActivityList.as_view(), name='activity_list'),
    path('activity/<int:pk>', views.ActivityDetail.as_view(), name='activity_detail'),

    path('item/', views.ItemList.as_view(), name='item_list'),
    path('item/<int:pk>', views.ItemDetail.as_view(), name='item_detail'),
]