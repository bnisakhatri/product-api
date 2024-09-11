from django.contrib import admin

# Register your models here.
from api_app.models import Category, Product

admin.site.register ({Category, Product})
