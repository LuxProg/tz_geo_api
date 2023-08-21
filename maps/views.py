from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.serializers import serialize
from .models import TblAzs, TblRoads
from .serializers import RoadSerializer, RoadAttrSerializer, AzsGeoSerializer, AllRoadsSerializer


def maps_home(request):
    maps = TblAzs.objects.order_by('id')
    return render(request, 'maps/maps_home.html', {'maps': maps})


def main_map(request):
    return render(request, 'maps/main_map.html')


# api1
class RoadGeometryAPIView(generics.ListAPIView):
    queryset = TblRoads.objects.all()
    serializer_class = AllRoadsSerializer


# api2
class RoadGeometryDetailView(generics.RetrieveAPIView):
    queryset = TblRoads.objects.all()
    serializer_class = RoadSerializer
    lookup_field = 'road_code'


# api3
class RoadAttrView(generics.RetrieveAPIView):
    queryset = TblRoads.objects.all()
    serializer_class = RoadAttrSerializer
    lookup_field = 'road_code'


# api4
class AzsFixedApi(generics.ListAPIView):
    serializer_class = AzsGeoSerializer

    def get_queryset(self):
        road_code = self.kwargs['road_code']
        return TblAzs.objects.filter(road_code=road_code)
