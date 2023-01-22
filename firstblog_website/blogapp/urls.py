from django.urls import path,re_path
from blogapp import views

urlpatterns = [
    re_path(r'login/', views.LoginView,name = 'login'),
    re_path(r'newpost/', views.NewPostView,name = 'newpost'),
    re_path(r'drafts/',views.DraftsListView,name = 'drafts'),
    re_path(r'draftview/(?P<pk>\d+)/', views.DraftsView,name = 'draftview'),
    re_path(r'postview/(?P<pk>\d+)/', views.PostView,name = 'post'),
    re_path(r'logout/', views.LogoutView,name = 'logout'),
    re_path(r'editpost/(?P<pk>\d+)/', views.EditPostView,name = 'editpost'),
    re_path(r'deletepost/(?P<pk>\d+)/', views.DeletePostView,name = 'deletepost'),
    re_path(r'newcomment/(?P<pk>\d+)/', views.NewCommentView,name = 'newcomment'),
    re_path(r'appcomm/(?P<pk>\d+)/', views.ApproveCommentView,name = 'appcomm'),
    re_path(r'delcomm/(?P<pk>\d+)/', views.DeleteCommentView,name = 'delcomm'),
]
