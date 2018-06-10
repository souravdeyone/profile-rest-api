from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()

router.register('Hello-viewset', views.HelloViewSets, base_name= 'hello-viewset')


urlpatterns = [

    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls))
]
