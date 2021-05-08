from datetime import datetime

from django.db import models
from rs.realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(verbose_name="title", max_length=200)
    address = models.CharField(verbose_name="address", max_length=200)
    city = models.CharField(verbose_name="city", max_length=100)
    state = models.CharField(verbose_name="state", max_length=100)
    zipcode = models.CharField(verbose_name="zip code", max_length=20)
    description = models.TextField(verbose_name="description", blank=True)
    price = models.IntegerField(verbose_name="price")
    bedrooms = models.IntegerField(verbose_name="bedrooms")
    bathrooms = models.DecimalField(
        verbose_name="bathroms", max_digits=2, decimal_places=1
    )
    garage = models.IntegerField(verbose_name="garage", default=0)
    sqft = models.IntegerField(verbose_name="sqft")
    lot_size = models.DecimalField(
        verbose_name="lot size", max_digits=5, decimal_places=1
    )
    photo_main = models.ImageField(
        verbose_name="photo main", upload_to="photos/%Y/%m/%d/"
    )
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_5 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_6 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    is_published = models.BooleanField(verbose_name="is published?", default=True)
    list_date = models.DateTimeField(
        verbose_name="list date", default=datetime.now, blank=True
    )

    def __str__(self) -> str:
        return self.title
