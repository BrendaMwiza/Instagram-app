from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^$',views.index,name ='welcome'),
    url(r'^new/picture$', views.new_pic, name='addPic')
]