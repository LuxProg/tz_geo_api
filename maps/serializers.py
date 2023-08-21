from rest_framework import serializers
# from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import TblRoads, TblAzs


# api1
class AllRoadsSerializer(serializers.Serializer):
    name = serializers.CharField()
    geomtype = serializers.CharField()
    coordinates = serializers.CharField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        geojson_v = {
            "type": "Feature",
            "geometry": {
                "type": data.pop("geomtype"),
                "coordinates": data.pop("coordinates")
            },
            "properties": data
        }
        return geojson_v


# api2
class RoadSerializer(serializers.Serializer):
    road_code = serializers.CharField()
    name = serializers.CharField()
    length_km = serializers.FloatField()
    geomtype = serializers.CharField()
    coordinates = serializers.CharField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        geojson_v = {
            "type": "Feature",
            "geometry": {
                "type": data.pop("geomtype"),
                "coordinates": data.pop("coordinates")
            },
            "properties": data
        }
        return geojson_v


# api3
class RoadAttrSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblRoads
        fields = ('road_code', 'name', 'length_km')


# api4
class AzsGeoSerializer(serializers.Serializer):
    geomtype = serializers.CharField()
    coordinates = serializers.CharField()
    road_code = serializers.CharField()
    id = serializers.IntegerField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        geojson_v = {
            "type": "Feature",
            "geometry": {
                "type": data.pop("geomtype"),
                "coordinates": data.pop("coordinates")
            },
            "properties": data
        }
        return geojson_v
