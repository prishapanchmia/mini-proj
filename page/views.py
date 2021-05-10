from django.shortcuts import render,get_object_or_404,redirect

from django.shortcuts import render

from .models import Article, Comment, Profile, Help
from django.http import Http404
from django.urls import reverse
from covid import Covid
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .utils import get_plot

from django.views.generic import(
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
	)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import image
# credentials  --> put your credentials here

def ProfileView(request,user):
	#user = request.user
	template_name = 'profile.html'
	queryset = get_object_or_404(Profile,user=user)
	articles = Article.objects.filter(user = queryset.user)
	context = {
	'qs' : queryset,
	'articles' : articles
	}
	return render(request,template_name,context)



def ArticleListViewMild(request):
	qs = Article.objects.filter(type_of_case__icontains='Mild')
	qs = qs.filter(verified=True)
	template_name='Mild.html'
	keyword_search = request.GET.get("search_keyword")

	if keyword_search != '' and keyword_search is not None:
		qs=qs.filter(name__icontains=keyword_search) | qs.filter(city__icontains=keyword_search )|qs.filter(state__icontains=keyword_search)|qs.filter(description__icontains=keyword_search)


	context = {
	"qs" : qs
	}

	return render(request,template_name,context )

def ArticleListViewModerate(request):
	qs = Article.objects.filter(type_of_case__icontains='Moderate')
	qs = qs.filter(verified=True)
	template_name='Moderate.html'

	keyword_search = request.GET.get("search_keyword")

	if keyword_search != '' and keyword_search is not None:
		qs=qs.filter(name__icontains=keyword_search) | qs.filter(city__icontains=keyword_search )|qs.filter(state__icontains=keyword_search)|qs.filter(description__icontains=keyword_search)


	context = {
	"qs" : qs
	}

	return render(request,template_name,context )

def ArticleListViewSevere(request):
	qs = Article.objects.filter(type_of_case__icontains='Severe')
	template_name='Severe.html'
	keyword_search = request.GET.get("search_keyword")

	if keyword_search != '' and keyword_search is not None:
		qs=qs.filter(name__icontains=keyword_search) | qs.filter(city__icontains=keyword_search )|qs.filter(state__icontains=keyword_search)|qs.filter(description__icontains=keyword_search)

	context = {
	"qs" : qs
	}

	return render(request,template_name,context )

def HelpListView(request):
	qs = Help.objects.all()
	template_name='help_list.html'
	help_search = request.GET.get("help_type")
	city_search = request.GET.get("city")
	locality_search = request.GET.get('locality')
	if city_search != '' and city_search is not None:
		qs=qs.filter(city__icontains=city_search) 
	if help_search != '' and help_search is not None:
		qs = qs.filter(category__icontains= help_search)
	if locality_search != '' and locality_search is not None:
		qs = qs.filter(locality__icontains = locality_search)
	context = {
	"qs" : qs
	}

	return render(request,template_name,context )

def ArticleDetailView(request,id):
	template_name='article_detail.html'
	queryset = get_object_or_404(Article,id=id)
	context = {
	"queryset" : queryset
		}
	return render(request,template_name,context)

def HelpDetailView(request,id):
	template_name='help_detail.html'
	queryset = get_object_or_404(Help,id=id)
	context = {
	"queryset" : queryset
		}
	return render(request,template_name,context)

def HelpCreateView(request):
	template_name = "yourhelp.html"
	my_form = Help()

	if request.method == "POST":
		my_form = Help(user = request.user,
			poc = request.POST.get("poc"),
			state  = request.POST.get("state"),
			city = request.POST.get("city"),
			locality = request.POST.get("locality"),
			category = request.POST.get("category"),
			description = request.POST.get("description")
			)
		my_form.save()

		context = {
		'queryset' : my_form
		}
		return render(request,'help_detail.html',context)

	context = {
	"form" : my_form
	}
	return render(request,template_name,context)

def ArticleCreateView(request):
	template_name = 'yourTestimonial.html'
	queryset=Article.objects.all()
	my_form=Article()

	if request.method=="POST":
		my_form=Article(user = request.user,name= request.POST.get("Name"),
		email = request.POST.get("Email"),
		state =	request.POST.get("State"),
		city =	request.POST.get("City"),
		type_of_case =	request.POST.get("Type_of_case"),
		age_group =		request.POST.get("Age_group"),
		description =	request.POST.get("Description"),
        
       # datetime = request.POST.get("DateTime")
		)

		files = request.FILES['myfile']
		print(str(files))
		my_form.file = files
		my_form.save()
		
		if image.check(str(files)):
			my_form.verified = True
			print("True")
		else:
			my_form.verified = False
			print("False")
		my_form.save()
		context={
		"queryset" : my_form
		}
		return render(request,'article_detail.html',context)

		# if my_form.is_valid():
		# 	my_form.save()
		# 	my_form=ArticleForm()
		# else:
		# 	print(my_form.errors)

	#return render(request,my_form.get_absolute_url(),{})
	context={
	"form" : my_form
	}

	return render(request,template_name,context)

def AddCommentView(request,id):
	model = Comment()
	article = get_object_or_404(Article,id=id)
	template_name = "add_comment.html"
	if request.method == 'POST':
		model = Comment(user = request.user,body = request.POST['comment'],article = article)
		model.save()
		context = {
		"queryset":article
		}	
		return render(request,'article_detail.html',context)
	return render(request, template_name)

def ArticleUpdateView(request,id):
	template_name = 'yourTestimonialupdate.html'
	my_form = get_object_or_404(Article,id=id)
	context={
	"form" : my_form
	}

	return render(request,template_name,context)



class ArticleDeleteView(DeleteView):
	template_name='article_delete.html'
	queryset = Article.objects.all()

	def get_object(self):
		my_id=self.kwargs.get("id")
		return get_object_or_404(Article,id=my_id)

	def get_success_url(self):
		return reverse('page:page-list')
# def clean_tweet(tweet):
#     	#return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \\t])|(\\w+:\\/\\/\\S+)', ' ', tweet).split())
# 		return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \\t)|(\\w+:\\/\\/\\S+)',' ',tweet).split())

def ArticleMainPage(request):
	covid = Covid()
	covid = Covid(source="worldometers")
	data = covid.get_data()
	i_dict = {}

	for i in data:
		if i['country'] == 'India':
			i_dict = i
		
			break

	df1 = pd.read_csv('coviddata.csv')
	groups = df1.groupby('State/UnionTerritory').agg({'Confirmed':'sum'}).sort_values(by='Confirmed',ascending=False).head(10)
	x , y = list(groups.Confirmed.index) , list(groups.Confirmed.values)
	context ={
	"qs" : i_dict,
	"x":x,
	"y":y
	}
	return render(request,'index.html',context)

def ArticleAll(request):
	return render(request,"testimonials.html",{})

def ArticleOurTeam(request):
	return render(request,"ourTeam.html",{})
# class ArticleListView(ListView):
# 	template_name = 'page/article_list.html'
# 	queryset = Article.objects.all()
