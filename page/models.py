from django.db import models
from django.urls import reverse
# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User

class Help(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
	category = models.CharField(max_length=12,default="",null=False,blank=True)
	state =	models.CharField(max_length=20,default="",null=False,blank=False)
	city =	models.CharField(max_length=20,default="",null=False,blank=False)
	locality = models.CharField(max_length=20,default="",null=False,blank=False)
	poc = models.CharField(max_length=20,default="",null=False,blank=False)
	description = models.TextField(default="",null=False,blank=True)

	def __str__(self):
		return f'{self.user} {self.id}'

	def get_absolute_url(self):
		return reverse("page:page-detail_help",kwargs={"id":self.id})

class Article(models.Model):
	# OPTIONS =(('Upto 18','Upto 18'),('19-30','19-30'),('31-50','31-50')
	# 	,('51-60','51-60'),('61-70','61-70'),('71 and older','71 and older'),)
	# OPTIONS1 =(('Mild','Mild'),
	# ('Moderate','Moderate'),
	# ('Severe','Severe'),)
	user = models.ForeignKey(User,
		on_delete=models.CASCADE,blank=True,null=True)
	name = models.CharField(max_length=25,default="",null=False,blank=False)
	email = models.EmailField(default="",null=False,blank=False)
	state =	models.CharField(max_length=20,default="",null=False,blank=False)
	city =	models.CharField(max_length=20,default="",null=False,blank=False)
	type_of_case =	models.CharField(max_length=20, default="")
	age_group =		models.CharField(max_length=20, default="")
	description =	models.TextField(default="",null=False,blank=False)
	verified = models.BooleanField(default=False)
	file = models.FileField(upload_to ='uploads/')

	def __str__(self):
		return f'{self.user} {self.id}'
	def get_absolute_url(self):
		return reverse("page:page-detail",kwargs={"id":self.id})

	def get_delete_url(self):
		return reverse("page:page-delete",kwargs={"id":self.id})

	def get_update_url(self):
		return reverse("page:page-update",kwargs={"id":self.id})

class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE)
	article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' %(self.article.name,self.user)

class Help_Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE)
	Help = models.ForeignKey(Help,on_delete=models.CASCADE,related_name='comments')
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s' %(self.user)

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg',upload_to='profile_pics')
	def __str__(self):
		return f'{self.user.username} Profile'