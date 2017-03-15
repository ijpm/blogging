"""blogging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from blogs.views import blogs_list, posts_list, post_detail, NewPostView, NewBlogView, PostListView
from users.views import LoginView, logout, RegisterView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blogs$', blogs_list, name="blogs_list"),
    url(r'^posts/new$', NewPostView.as_view(), name="new_post"),
    url(r'^posts/mis-posts$', PostListView.as_view(), name="new_post"),
    url(r'^blogs/new$', NewBlogView.as_view(), name="new_blog"),
    url(r'^posts/(?P<post_pk>[0-9]+)$', post_detail, name="post_detail"),
    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'^sign-up', RegisterView.as_view(), name="registro"),
    url(r'^logout$', logout, name="logout"),
    url(r'^$', posts_list, name="home")
]