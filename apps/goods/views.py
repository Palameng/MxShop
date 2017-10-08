# -*- coding: utf-8 -*-
from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response    # 该处是django REST framework 的Response,比django的强大很多
from .models import Goods
from rest_framework import status, generics, mixins
from rest_framework.pagination import PageNumberPagination

from rest_framework import viewsets
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
