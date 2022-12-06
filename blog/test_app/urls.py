from django.urls import path
from . import views


urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('create',views.create,name='create'),
    path('post/<int:pk>/update',views.post_update,name='news_update'),
    path('post/<int:pk>/delete',views.NewsDeleteView.as_view(),name='news_delete'),
    path('post/<int:pk>/comment',views.post_comment,name='post_comment'),
    path('personal',views.personal,name='personal'),

]