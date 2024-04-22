from django.contrib import admin
from apps.exec import export_to_xlsx
# from apps.models import Product, Order, NewOrder, Profile
from apps.models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'description')
#     search_fields = ('name', 'price', 'description')
#
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product', 'quantity', 'status')
#     search_fields = ('user', 'product', 'quantity', 'status')
#     list_filter = ('user', 'product', 'quantity', 'status')
#
#
# @admin.register(NewOrder)
# class NewOrderAdmin(admin.ModelAdmin):
#     list_display = 'user', 'product', 'date', 'status'
#     list_display_links = 'id'
#
#     def get_queryset(self, request):
#         return super().get_queryset(request).filter(status=Order.Status.NEW)
