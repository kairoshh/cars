from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet

from mainapp.serializers import(
    CarModel, CarModelSerializer,
)
from mainapp.models import (
    CarMark,
)
from mainapp.serializers import (
    CarMarkSerializers, CarModelSerializer
)

from rest_framework.response import Response

class CarModelView(ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

class CarMarkView(APIView):

    def post(self, request):
        serializers = CarMarkSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        data = serializers.validated_data 
        name = data.get('name')
        country = data.get('country')
        date_created = data.get('date_created')
        cars = CarMark.objects.create(
            name=name, country=country, date_created=date_created
        )
        return Response(CarMarkSerializers(instance=cars, many=True).data)
    
    def get(self, request):
        cars = CarMark.objects.all()
        serializers = CarMarkSerializers(instance=cars, many=True).data

        return Response(serializers)
