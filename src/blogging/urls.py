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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from blogs.api import BlogViewSet, PostViewSet
from blogs.views import blogs_list, posts_list, post_detail, NewPostView, NewBlogView, PostListView, BlogListView, \
    post_detail_blog
from users.api import UserViewSet
from users.views import LoginView, logout, RegisterView


router = DefaultRouter()
router.register("users", UserViewSet, base_name="users_api")
router.register("blogs", BlogViewSet, base_name="blogs_api")
router.register("posts", PostViewSet, base_name="posts_api")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blogs$', blogs_list, name="blogs_list"),
    url(r'^posts/new$', NewPostView.as_view(), name="new_post"),
    url(r'^posts/mis-posts$', PostListView.as_view(), name="mis_posts"),
    url(r'^posts/mis-blogs$', BlogListView.as_view(), name="mis_blogs"),
    url(r'^blogs/new$', NewBlogView.as_view(), name="new_blog"),
    url(r'^blogs/(?P<blog_name>[a-zA-Z-]+)/(?P<post_pk>[0-9]+)$', post_detail, name="post_detail"),
    url(r'^blogs/(?P<blog_pk>[0-9]+)/$', post_detail_blog, name="post_from_blog"),
    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'^sign-up', RegisterView.as_view(), name="registro"),
    url(r'^logout$', logout, name="logout"),
    url(r'^$', posts_list, name="home"),

    url(r'^api/1.0/', include(router.urls))
]