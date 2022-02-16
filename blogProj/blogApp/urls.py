from django.urls import path
from . import views
from .views import AddCommentView, LikeView


urlpatterns = [

    path('home', views.home, name='home'),
    path('admin-portal', views.admin_portal, name='admin-portal'),
    path('post', views.post, name='post'),
    path('postDetails/<post_id>', views.postDetails, name='postDetails'),
    path('addPost', views.addPost, name='addPost'),
    path('deletePost/<post_id>', views.deletePost, name='deletePost'),
    path('editPost/<post_id>', views.editPost, name='editPost'),
    # path('addComment/<post_id>',views.addComment , name='addComment'),
    path('addComment/<int:pk>/', AddCommentView.as_view(), name='addComment'),

    # likePost URl
    path('like/<post_id>', LikeView, name='like_post'),
    # auth urls
    path('login', views.loginPg, name='login'),
    path('signup', views.signupPg, name='signup'),
    path('signout', views.signoutPg, name='signout'),

    # category usrls
    path('sports/', views.redirectSports, name='redirect_sports'),
    path('news/', views.redirectNews, name='redirect_news'),
    path('politics/', views.redirectPolitics, name='redirect_politics'),
]
