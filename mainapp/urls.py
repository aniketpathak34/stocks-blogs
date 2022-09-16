
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.stockPicker, name = 'stockpicker'),
    path('stocktracker/', views.stockTracker, name = 'stocktracker'),
    path('home1/', views.PostList.as_view(), name='home1'),
    path('post_detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('addPost1/', views.AddPostView.as_view(), name='addPost1'),  
    path('Post_detail/edit/<slug:slug>/', views.UpdatePostView.as_view(), name='updatePost'),
    path('Post_detail/<slug:slug>/remove', views.DeletePostView.as_view(), name='deletePost'),
    path('like/<slug:slug>', views.LikeView, name='like_post'),
    path('article/<slug:pk>/comment/', views.AddCommentView.as_view(), name='add_comment'),
] 