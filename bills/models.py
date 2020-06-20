from django.db import models

# Create your models here.
class AbstractBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    soft_delete = models.BooleanField(default=False,db_index=True)

    class Meta:
        abstract = True


class Item(AbstractBase):
	code = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	price = models.FloatField(default=0.0)

	def __str__(self):
		return str(self.name)


class Discountrule(AbstractBase):
	coupon = models.CharField(max_length=50)
	purchased_item_code = models.CharField(max_length=50)
	min_purchased_item_required = models.IntegerField(default=1)
	discounted_item_code = models.CharField(max_length=50)
	discounted_price = models.FloatField(blank=True, null=True)
	discount_percent = models.FloatField(blank=True, null=True)
	discounted_item_limit = models.IntegerField(blank=True, null=True)
	discounted_item_limit_percent = models.FloatField(blank=True, null=True)

	def __str__(self):
		return str(self.coupon)