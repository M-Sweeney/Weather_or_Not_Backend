from rest_framework import serializers
from .models import User, Category, Item, Activity


class UserSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(
      view_name = 'category_detail',
      many = True,
      read_only = True
    )
    item = serializers.HyperlinkedRelatedField(
      view_name = 'item_detail',
      many = True,
      read_only = True
    )
    activity = serializers.HyperlinkedRelatedField(
      view_name = 'activity_detail',
      many = True,
      read_only = True
    )
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'city', 'item', 'category', 'activity')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta: 
        model = Category
        fields=('id', 'name', 'user')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer( read_only=True)

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'photo', 'hot', 'warm', 'cool', 'cold', 'rain', 'snow', 'wind', 'category', 'user')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = ('id', 'name', 'description', 'free', 'indoors', 'users')


