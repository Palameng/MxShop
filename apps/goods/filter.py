from rest_framework import generics
import django_filters
from .models import Goods
from django.db.models import Q


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    pricemin = django_filters.NumberFilter(name="shop_price", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')
    # name = django_filters.CharFilter(name='name', lookup_expr='icontains')  # 模糊查询

    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        queryset = queryset.filter(
                                    Q(category_id=value) |
                                    Q(category__parent_category_id=value) |
                                    Q(category__parent_category__parent_category_id=value)
                                   )
        return queryset

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'name']
