# -*- coding: utf-8 -*-
from django.views.generic.base import View
from .models import Goods
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
import json


class GoodsListView(View):
    def get(self, request):
        """
        商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]
        # 使用遍历方法填充json_dict
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)

        # 使用model_to_dict方法
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)

        json_list = serializers.serialize('json', goods)
        json_list = json.loads(json_list)

        return JsonResponse(json_list, safe=False)
