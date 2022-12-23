from rest_framework import serializers
from .models import User, Category, Item, Activity


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
      view_name = 'user_detail',
      many = True,
      read_only = True,
      source='users'
    )

    class Meta: 
        model = Category
        fields=('id', 'name', 'user')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
      view_name = 'user_detail',
      many = True,
      read_only = True,
      source='users'
    )

    category = serializers.HyperlinkedRelatedField(
      view_name = 'category_detail',
      many = True,
      read_only = True,
      source='categories'
    )

    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'photo', 'hot', 'warm', 'cool', 'cold', 'rain', 'snow', 'wind', 'category', 'user')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
      view_name = 'user_detail',
      many = True,
      read_only = True,
      source='users'
    )

    class Meta:
        model = Activity
        fields = ('id', 'name', 'description', 'free', 'indoors', 'user')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(
      many = True,
      read_only = True,
      source='categories'
    )
    item = ItemSerializer(
      many = True,
      read_only = True,
      source='items' 
    )
    activity = ActivitySerializer(
      many = True,
      read_only = True,
      source='activities'
    )
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'city', 'item', 'category', 'activity')