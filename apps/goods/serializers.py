# -*- coding: utf-8 -*-
from rest_framework import serializers


class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, max_length=100)
    click_num = serializers.IntegerField(default=0)
    # 当使用ImageField或者是文件类型时，drf会判断到是媒体类型，所以回去查找setting.py中的MEDIA路径，并加到路径头部
    goods_front_image = serializers.ImageField()
