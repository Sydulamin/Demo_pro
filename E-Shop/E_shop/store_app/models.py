from django.db import models
from django.utils import timezone


class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Filter_Price(models.Model):
    FILTER_PRICE = (
        ('1000 TO 10000', '1000 TO 10000'),
        ('10000 TO 20000', '10000 TO 20000'),
        ('20000 TO 30000', '20000 TO 30000'),
        ('30000 TO 40000', '30000 TO 40000'),
        ('40000 TO 50000', '40000 TO 50000'),
        ('50000 TO 60000', '50000 TO 60000'),
        ('60000 TO 70000', '60000 TO 70000'),
        ('70000 TO 80000', '70000 TO 80000'),
        ('80000 TO 90000', '80000 TO 90000'),
        ('90000 TO 100000', '90000 TO 100000'),
    )
    price = models.CharField(choices=FILTER_PRICE, max_length=60)

    def __str__(self):
        return self.price


class Product(models.Model):
    CONDITION = (('New', 'New'), ('Old', 'Old'))
    STOCK = (('IN_STOCK', 'IN_STOCK'), ('OUT_STOCK', 'OUT_STOCK'))
    STATUS = (('Publish', 'Publish'), ('Draft', 'Draft'))

    unique_id = models.CharField(unique=True, max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/img', default=())
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    condition = models.CharField(choices=CONDITION, max_length=100)
    information = models.TextField(max_length=500)
    description = models.TextField(max_length=500)
    stock = models.CharField(choices=STOCK, max_length=200)
    status = models.CharField(choices=STATUS, max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price, on_delete=models.CASCADE)

    def save(self,*args,**kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.name


class Images(models.Model):
    image = models.ImageField(upload_to='product_images/img')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
