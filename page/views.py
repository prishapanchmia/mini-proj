from django.shortcuts import render,get_object_or_404,redirect

from django.shortcuts import render

from .models import Article
from django.http import Http404
from django.urls import reverse
from covid import Covid


from django.views.generic import(
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
	)


# credentials  --> put your credentials here





def ArticleDetailView(request,id):
	template_name='page/article_detail.html'
	queryset = get_object_or_404(Article,id=id)
	context = {
	"queryset" : queryset
		}
	return render(request,template_name,context)

def ArticleListViewMild(request):
	qs = Article.objects.filter(type_of_case__icontains='Mild')
	template_name='page/Mild.html'
	keyword_search = request.GET.get("search_keyword")

	if keyword_search != '' and keyword_search is not None:
		qs=qs.filter(name__icontains=keyword_search) | qs.filter(city__icontains=keyword_search )|qs.filter(state__icontains=keyword_search)|qs.filter(description__icontains=keyword_search)


	context = {
	"qs" : qs
	}

	return render(request,template_name,context )

def ArticleListViewModerate(request):
	qs = Article.objects.filter(type_of_case__icontains='Moderate')
	template_name='page/Moderate.html'

	keyword_search = request.GET.get("search_keyword")

	if keyword_search != '' and keyword_search is not None:
		qs=qs.filter(name__icontains=keyword_search) | qs.filter(city__icontains=keyword_search )|qs.filter(state__icontains=keyword_search)|qs.filter(description__icontains=keyword_search)


	context = {
	"qs" : qs
	}

	return render(request,template_name,context )

def ArticleListViewSevere(request):
	qs = Article.objects.filter(type_of_case__icontains='Severe')
	template_name='page/Severe.html'
	keyword_search = request.GET.get("search_keyword")

	if keyword_search != '' and keyword_search is not None:
		qs=qs.filter(name__icontains=keyword_search) | qs.filter(city__icontains=keyword_search )|qs.filter(state__icontains=keyword_search)|qs.filter(description__icontains=keyword_search)

	context = {
	"qs" : qs
	}

	return render(request,template_name,context )

def ArticleCreateView(request):
	template_name = 'page/yourTestimonial.html'
	queryset=Article.objects.all()
	my_form=Article()

	if request.method=="POST":
		my_form=Article(name= request.POST.get("Name"),
		email = request.POST.get("Email"),
		state =	request.POST.get("State"),
		city =	request.POST.get("City"),
		type_of_case =	request.POST.get("Type_of_case"),
		age_group =		request.POST.get("Age_group"),
		description =	request.POST.get("Description"),
        
       # datetime = request.POST.get("DateTime")
		)
		my_form.save()
		context={
		"queryset" : my_form
		}
		return render(request,'page/article_detail.html',context)

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

	

class ArticleUpdateView(UpdateView):
	template_name = 'page/yourTestimonial.html'
	queryset=Article.objects.all()
	

	def get_object(self):
		my_id=self.kwargs.get("id")
		return get_object_or_404(Article,id=my_id)

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)

class ArticleDeleteView(DeleteView):
	template_name='page/article_delete.html'
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
	context ={
	"qs" : i_dict
	}
	return render(request,'page/index.html',context)

def ArticleAll(request):
	return render(request,"page/testimonials.html",{})

def ArticleOurTeam(request):
	return render(request,"page/ourTeam.html",{})
# class ArticleListView(ListView):
# 	template_name = 'page/article_list.html'
# 	queryset = Article.objects.all()
