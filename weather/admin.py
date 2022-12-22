from django.contrib import admin
from .models import Users, Items, Categories, Activities

admin.site.register(Users)
admin.site.register(Items)
admin.site.register(Categories)
admin.site.register(Activities)