from django.db import models
from django.urls import reverse
# Create your models here.



class Article(models.Model):
	# OPTIONS =(('Upto 18','Upto 18'),('19-30','19-30'),('31-50','31-50')
	# 	,('51-60','51-60'),('61-70','61-70'),('71 and older','71 and older'),)
	# OPTIONS1 =(('Mild','Mild'),
	# ('Moderate','Moderate'),
	# ('Severe','Severe'),)
	name = models.CharField(max_length=25,default="",null=False,blank=False)
	email = models.EmailField(default="",null=False,blank=False)
	state =	models.CharField(max_length=20,default="",null=False,blank=False)
	city =	models.CharField(max_length=20,default="",null=False,blank=False)
	type_of_case =	models.CharField(max_length=20, default="")
	age_group =		models.CharField(max_length=20, default="")
	description =	models.TextField(default="",null=False,blank=False)
	def get_absolute_url(self):
		return reverse("page:page-detail",kwargs={"id":self.id})

	def get_delete_url(self):
		return reverse("page:page-delete",kwargs={"id":self.id})

	def get_update_url(self):
		return reverse("page:page-update",kwargs={"id":self.id})