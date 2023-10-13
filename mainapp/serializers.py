from rest_framework import serializers

from mainapp.models import CarModel


class CarMarkSerializers(serializers.Serializer):
    name = serializers.CharField()
    country = serializers.CharField()
    date_created = serializers.IntegerField()


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = (
            'id','name','color',
            'year','max_speed',
            'horse_power','price',
            'cars',
        )

{
    "name":"BMW",
    "country":"Germany",
    "date_created":1999

}
