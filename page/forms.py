from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput())
	email = forms.EmailField(widget=forms.TextInput())
	state =	forms.CharField(widget=forms.TextInput())
	city =	forms.CharField(widget=forms.TextInput())
	type_of_case =	forms.CharField(widget=forms.TextInput())
	age_group 	=	forms.CharField(widget=forms.TextInput())
	description =	forms.CharField(widget=forms.Textarea())

	class Meta:
		model=Article
		fields=['name','email','state','city','type_of_case',
		'age_group','description']
