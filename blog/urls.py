"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include

from blog.views import Home, post_detail, add_post, edit_post, del_post, signup

urlpatterns = [
    url(r'^$',Home,name="Home"),
    url(r'^(?P<pk>[0-9]+)/$', post_detail, name="post"),
    url(r'^add/$',add_post,name="add_post"),
    url(r'^edit/(?P<pk>[0-9]+)/$',edit_post,name="edit_post"),
    url(r'^(?P<id>[0-9]+)/delete/',del_post, name= "delete_post"),

]



