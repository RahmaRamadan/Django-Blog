from django.urls import path
from . import views

urlpatterns = [

    path('home',views.home, name='home'),
    #auth urls
    path('login',views.loginPg , name='login'),
    path('signup',views.signupPg , name='signup'),
    path('signout',views.signoutPg , name='signout'),
    #category usrls
    path('sports/',views.redirectSports , name='redirect_sports'),
    path('news/',views.redirectNews , name='redirect_news'),
    path('politics/',views.redirectPolitics , name='redirect_politics'),

]