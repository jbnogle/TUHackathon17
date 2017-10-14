# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^refer/$' , views.AboutPageView.as_view()), 
    url(r'^popup/$' , views.PopupPageView.as_view()),
    url(r'^accept/$', views.AcceptPageView.as_view()),
    url(r'^stats/$' , views.StatsPageView.as_view()),
]
