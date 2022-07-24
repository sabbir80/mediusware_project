from django.contrib import admin
from django.utils.html import format_html

from .models import *
from django.urls import reverse
from django.utils.http import urlencode
# Register your models here.
# admin.site.register(Variant)
# admin.site.register(Product)
# admin.site.register(ProductVariant)
# admin.site.register(ProductVariantPrice)
# admin.site.register(ProductImage)

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ('title','description','active','test_variant')
    list_filter = ['title']
    search_fields = ['title__icontains']

    def test_variant(self,obj):
        return 'variant'+'_'+obj.title

@admin.register(ProductVariant)
class ProductVarianAdmin(admin.ModelAdmin):
    list_display = ('variant_title', 'product','variant','variant_link')
    def variant_link(self,obj):
        url = (
            reverse("admin:product_variant_changelist")
            + "?"
            + urlencode({"variant__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">Variant</a>', url)


