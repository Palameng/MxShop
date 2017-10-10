# -*- coding: utf-8 -*-
from .serializers import GoodsSerializer, CategorySerializer
from rest_framework.views import APIView

# 该处是django REST framework 的Response,比django的强大很多
from rest_framework.response import Response

from .models import Goods, GoodsCategory
from rest_framework import status, generics, mixins
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .filter import GoodsFilter
from rest_framework import filters
# Create your views here.


# 继承APIView实现的方式

# class GoodsListView(APIView):
#     """
#     List all goods.
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]    # QuerySet instance
#         goods_serializer = GoodsSerializer(goods, many=True)  # Json(Serializer) instance
#         return Response(goods_serializer.data)
#
#     def post(self, request, format=None):
#         goods_serializer = GoodsSerializer(data=request.data)
#         if goods_serializer.is_valid():
#             goods_serializer.save()     # 此处会调用GoodsSerializer中的create方法
#             return Response(goods_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(goods_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 继承GenericAPIView实现的方式

# class GoodsListView(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     generics.GenericAPIView):
#     """
#     商品列表页
#     """
#     queryset = Goods.objects.all()[:10]
#     serializer_class = GoodsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# 定制序列化数据的分页
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


# 继承ListAPIView实现的方式

# class GoodsListView(generics.ListAPIView):
#     """
#     商品列表页
#     """
#     # queryset = Goods.objects.all()[:10]
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsPagination


# 使用ViewSet方法实现的方式
class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

    # 设置支持的过滤类型
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

    # 注册search_fields提供搜索功能
    search_fields = ('name', 'goods_brief', 'goods_desc')

    # 注册filter_class 或 filter_fields 提供过滤功能
    filter_class = GoodsFilter
    # filter_fields = ('name', 'shop_price')

    # 注册ordering_fields提供排序功能
    ordering_fields = ('sold_num', 'add_time')

    # def get_queryset(self):
    #     """
    #     简单的过滤操作
    #     :return:
    #     """
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get('price_min', 0)
    #     if price_min:
    #         queryset = queryset.filter(shop_price__gt=int(price_min))
    #     # return Goods.objects.filter(shop_price__gt=100)
    #     return queryset


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    """
    # queryset = GoodsCategory.objects.all()
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
