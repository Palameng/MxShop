"""MxShop URL Configuration

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
from rest_framework_jwt.views import obtain_jwt_token
# from django.contrib import admin
import xadmin
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListViewSet, CategoryViewSet
from users.views import SmsCodeViewset
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

route = DefaultRouter()

# 配置goods的url
route.register(r'goods', GoodsListViewSet, 'goods')

# 配置category的url
route.register(r'categorys', CategoryViewSet, 'categorys')

# 配置verifycode的url
route.register(r'codes', SmsCodeViewset, 'codes')

# good_list = GoodsListViewSet.as_view({
#     'get': 'list',
# })

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # 实现了DRF的登录
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # goods list view
    # url(r'goods/$', GoodsListView.as_view(), name="goods-list"),
    # url(r'goods/$', good_list, name="goods-list"),

    url(r'^', include(route.urls)),
    url(r'docs/', include_docs_urls(title="MxShop")),

    # drf的自带token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),  # 向这个url POST一个用户名密码生成Token

    # jwt的认证接口，修改成login是因为Vue那边触发登录的url为/login/
    url(r'^login/', obtain_jwt_token),
]
