from django.contrib import admin
from .models import Slider, BannerArea, Category, Main_Category,\
    Sub_Category, Product, Addtional_Iformation, Product_Image, Section, Accessories, Color,\
    Codon_copon
# Register your models here.


class Product_images_turbline(admin.TabularInline):
    model = Product_Image


class Addtional_Iformation_tuberline(admin.TabularInline):
    model = Addtional_Iformation


class Accessories_tuberline(admin.TabularInline):
    model = Accessories


class Accessory_Admin(admin.ModelAdmin):
    inlines = (Accessories_tuberline)
    list_display = ('name', 'product', 'color')


class Product_Admin(admin.ModelAdmin):
    inlines = (Product_images_turbline,
               Addtional_Iformation_tuberline, Accessories_tuberline)
    list_display = ('name', 'price', 'category', 'section')
    list_editable = ('category', 'section')


admin.site.register(Product, Product_Admin)

admin.site.register(
    [Slider, BannerArea,
     Main_Category, Category,
     Sub_Category, Section,
     Product_Image, Addtional_Iformation, Accessories, Color, Codon_copon])
