from drf_yasg import openapi

response_schema_dict = {
    "200": openapi.Response(
        description="Operação realizada com sucesso.",
        examples={
            "application/json": {
                "message": "Operation performed successfully.",
                "detail": "Location identified: 0.\nLocation not identified: 0."
            }
        }
    )
}
