from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Slider(models.Model):
    DISCOUNT_DEAL = (('HOT ARRIVAL', 'HOT ARRIVAL'),
                     ('NWE ARRIVAL', 'NEW ARRIVAL')
                     )
    image = models.ImageField(upload_to='slider', default="noprofile.png")
    Discount_Deal = models.CharField(max_length=100, choices=DISCOUNT_DEAL)
    brand_name = models.CharField(max_length=100)
    Discount = models.IntegerField()
    sale = models.IntegerField
    link = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = ("Slider")
        verbose_name_plural = ("Sliders")

    def __str__(self):
        return self.brand_name


class BannerArea(models.Model):
    image = models.ImageField(upload_to='BannerArea', default="noprofile.png")
    Discount_Deal = models.CharField(max_length=100)
    quote = models.CharField(max_length=100)
    Discount = models.IntegerField()
    link = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = ("BannerArea")
        verbose_name_plural = ("BannerAreas")

    def __str__(self):
        return self.quote


class Main_Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Main_Category")
        verbose_name_plural = ("Main_Categorys")

    def __str__(self):
        return self.name


class Category(models.Model):
    main_category = models.ForeignKey(Main_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name+"---- "+self.main_category.name


class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Sub_Category")
        verbose_name_plural = ("Sub_Categories")

    def __str__(self):

        return self.name+"----"+self.category.name + "----" + self.category.main_category.name


class Section(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Section")
        verbose_name_plural = ("Sections")

    def __str__(self):
        return self.name


class Color(models.Model):
    code = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("color")
        verbose_name_plural = ("colors")

    def __str__(self):
        return self.code


class Product(models.Model):
    total_quantity = models.IntegerField()
    avalabilty = models.IntegerField()
    faturated_image = models.CharField(max_length=100)
    Discount = models.IntegerField()
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    tax = models.IntegerField(null=True)
    packing_cost = models.IntegerField(null=True)
    color = models.CharField(max_length=12, default='red')
    information = models.TextField(max_length=2000)
    product_model = models.CharField(max_length=100)
    Description = models.TextField(max_length=2000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Tags = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Codon_copon(models.Model):
    condon = models.CharField(max_length=100)
    Discount = models.IntegerField()

    class Meta:
        verbose_name = ("Codon_copon")
        verbose_name_plural = ("Codon_copons")

    def __str__(self):
        return self.condon


class Product_Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Product_Image")
        verbose_name_plural = ("Product_Images")

    def __str__(self):
        return self.product.name


class Addtional_Iformation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specfication = models.CharField(max_length=100)
    details = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Addtional_Iformation")
        verbose_name_plural = ("Addtional_Iformations")

    def __str__(self):
        return self.product.name


class Accessories(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='accessory')
    image_url = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=12, default='red')

    class Meta:
        verbose_name = ("Accessories")
        verbose_name_plural = ("Accessoriess")

    def __str__(self):
        return self.product.name
