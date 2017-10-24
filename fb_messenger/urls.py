
from django.conf.urls import include, url
from .views import YoMamaBotView

urlpatterns = [

url(r'^XXX/?$', YoMamaBotView.as_view()) 



]


