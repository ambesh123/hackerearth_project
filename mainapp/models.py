from django.db import models

class User_auth(models.Model):
	username = models.CharField(max_length=20 , primary_key = True)
	email = models.CharField(max_length=20 )
	password = models.CharField(max_length=20)


class Winemag(models.Model):
	country = models.CharField(max_length=30)
	description = models.TextField(null = True)
	designation = models.CharField(max_length=30)
	points = models.CharField(max_length=10 , null = True)
	price = models.CharField(max_length=10)
	province = models.CharField(max_length=30 , null = True)
	region_1 = models.CharField(max_length=30 , null = True)
	region_2 = models.CharField(max_length=30 , null = True)
	variety = models.CharField(max_length=30 , null = True)
	winery = models.CharField(max_length=30 )

	def __str__(self):
		return self.winery

