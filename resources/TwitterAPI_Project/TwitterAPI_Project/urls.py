"""TwitterAPI_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from API import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^Followers/(?P<pk>[a-zA-Z0-9]+)',views.Apı_ClassList.as_view()),
    url('^getTT/(?P<pk>[a-zA-Z]+)',views.getTrendingTopic.as_view()),
    url('^block_user/(?P<pk>[a-zA-Z0-9]+)',views.block_user.as_view()),
    url('^followUser/(?P<pk>[a-zA-Z0-9]+)',views.followUser.as_view()),
    url('^PostTweet/(?P<pk>.*)',views.PostTweet.as_view()),
    url('^friends/(?P<pk>[a-zA-Z0-9]+)',views.friends.as_view()),
	url('^getFavorite/(?P<pk>[a-zA-Z0-9]+)',views.getFavorite.as_view()),
	url('^retweet/(?P<pk>[a-zA-Z0-9]+)',views.retweet.as_view()),

]

urlpatterns=format_suffix_patterns(urlpatterns)
