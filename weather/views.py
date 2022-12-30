from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserSerializer, ItemSerializer, CategorySerializer, ActivitySerializer
from .models import User, Category, Item, Activity

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ItemPost(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request):
        itemObj=Item.objects.all()
        itemSerializeObj=ItemSerializer(itemObj,many=True)
        return Response(itemSerializeObj.data)
    
    def post(self,request):
        serializeobj=ItemSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)

class ItemUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    def post(self,request,pk):
        try:
            itemObj=self.get_object()
        except:
            return Response("Not found in database")

        serializeobj=ItemSerializer(itemObj,data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)

class ItemDelete(generics.RetrieveUpdateDestroyAPIView):
    def post(self,request,pk):
        try:
            itemObj=Item.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        itemObj.delete()
        return Response(200)


class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer