from django.urls import path

from .views import (
	
	ArticleDetailView,
	ArticleCreateView,
	ArticleUpdateView,AddCommentView,
	ArticleDeleteView,ArticleMainPage
	,ArticleListViewSevere,ArticleListViewModerate
	,ArticleListViewMild,ArticleAll,ArticleOurTeam,ProfileView,HelpCreateView,HelpDetailView,
	HelpListView
)

app_name='page'

urlpatterns = [
path("",ArticleMainPage,name="page-home"),
#path("list/",ArticleListView,name="page-list"),
path("<int:id>/",ArticleDetailView,name="page-detail"),
path("<int:id>/delete/",ArticleDeleteView.as_view(),name="page-delete"),
path("<int:id>/update/",ArticleUpdateView.as_view(),name="page-update"),
path("create/",ArticleCreateView,name="page-create"),
path("create_help/",HelpCreateView,name="page-create_help"),
path("detail_help/<int:id>/",HelpDetailView,name="page-detail_help"),
path("list_help/",HelpListView,name="page-list_help"),
path("Mild/",ArticleListViewMild,name="page-Mild"),
path("Moderate/",ArticleListViewModerate,name="page-Moderate"),
path("Severe/",ArticleListViewSevere,name="page-Severe"),
path("testimonials/",ArticleAll,name="page-alltestimonials"),
path("ourteam/",ArticleOurTeam,name="page-ourteam"),
path("article/<int:id>/addcomment/",AddCommentView,name="page-addcomment"),
path("profile/",ProfileView,name="page-profile"),

]