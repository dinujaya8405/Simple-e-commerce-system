from django.contrib import admin

from .models import Product
from .models import Color
from .models import Category
from .models import SuperCategory
from .models import Order
from .models import Cart

admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Category)
admin.site.register(SuperCategory)
admin.site.register(Order)
admin.site.register(Cart)
