import pandas as pd
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
import sqlite3
from core.processing_file import processing_file
from customer.drf_yasg import response_schema_dict
from customer.models import Customers
from customer.serializer import CustomersSerializer
from oowlish.settings import BASE_DIR


class ImportDataView(APIView):

    @swagger_auto_schema(responses=response_schema_dict)
    def get(self, request, *args, **kwargs):
        sucess, not_found = processing_file()

        con = sqlite3.connect(f'{BASE_DIR}/db.sqlite3')

        data_customer = pd.DataFrame(sucess)
        data_customer.to_sql('oowlish_customers', con, if_exists='append', index=False)

        return Response({"message": "Operation performed successfully.",
                         "detail": f"Location identified: {len(sucess) - len(not_found)}.\n"
                                   f"Location not identified: {len(not_found)}."})


class CustomersViewset(ModelViewSet):

    serializer_class = CustomersSerializer
    queryset = Customers.objects.all()

    def get_queryset(self):
        return self.filter_queryset(self.queryset)

    def list(self, request, *args, **kwargs):
        """
        List all customers
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
