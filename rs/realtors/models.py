from datetime import datetime

from django.db import models


class Realtor(models.Model):
    name = models.CharField(verbose_name="name", max_length=200)
    photo = models.ImageField(verbose_name="photo", upload_to="photos/%Y/%m/%d/")
    description = models.TextField(verbose_name="description", blank=True)
    phone = models.CharField(verbose_name="phone", max_length=20)
    email = models.EmailField(verbose_name="e-mail")
    is_mvp = models.BooleanField(verbose_name="is mvp?", default=False)
    hire_date = models.DateTimeField(
        verbose_name="hire date", default=datetime.now, blank=True
    )

    def __str__(self) -> str:
        return self.name
