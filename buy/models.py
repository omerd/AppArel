from django.db import models
from django.contrib.auth.models import User

	
class ProductCatalog(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	price = models.PositiveIntegerField(default = 500)
	def __unicode__ (self): 
		return self.name

class Product(models.Model):
	"""A model of a rock band."""
	pid = models.BigIntegerField(primary_key=True)
	catalog = models.ForeignKey(ProductCatalog)
	#barcod id
	#RFID
	def __unicode__ (self): 
		return self.catalog.name + '-' + str(self.pid)
	
	
class BuyHistory(models.Model):
	product = models.ForeignKey(Product)
	customer = models.ForeignKey(User)
	date = models.DateField(auto_now_add=True, blank=True)
	time = models.TimeField(auto_now_add=True, blank=True)
	def __unicode__ (self): 
		return str(self.product) + '-' + str(self.customer) + '-' + str(self.date) + str(self.time)
