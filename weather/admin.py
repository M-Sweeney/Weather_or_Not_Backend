from django.contrib import admin
from .models import User, Item, Category, Activity

admin.site.register(User)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Activity)