from django.db import models

# Create your models here.
class Product(models.Model) :
    name = models.CharField(max_length=50, blank=True) # 이건 뭐여 있던디
    category = models.CharField(max_length=50, blank=True)
    manu_f =  models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    price_buy = models.CharField(max_length=50, blank=True)
    price_borrow = models.CharField(max_length=50, blank=True)
    url_go = models.URLField()

    def __str__(self) :
        return f'[{self.pk}]{self.name}'