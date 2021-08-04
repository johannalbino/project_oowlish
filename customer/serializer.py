from customer.models import Customers
from rest_framework.serializers import ModelSerializer


class CustomersSerializer(ModelSerializer):

    class Meta:
        model = Customers
        fields = '__all__'
