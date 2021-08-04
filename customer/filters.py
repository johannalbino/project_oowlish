from django_filters import rest_framework as filters
from customer.models import Customers


class CustomersFilter(filters.FilterSet):
    first_name = filters.CharFilter(lookup_expr="icontains")
    city = filters.CharFilter(lookup_expr="icontains")
    longitude = filters.CharFilter(lookup_expr="icontains")
    latitude = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Customers
        fields = ['first_name', 'city', 'longitude', 'latitude']
