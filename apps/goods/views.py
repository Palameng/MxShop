# -*- coding: utf-8 -*-
from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response    # 该处是django REST framework 的Response,比django的强大很多
from .models import Goods
# Create your views here.


class GoodsListView(APIView):
    """
    List all goods.
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]    # QuerySet instance
        goods_serializer = GoodsSerializer(goods, many=True)  # Json(Serializer) instance
        return Response(goods_serializer.data)
