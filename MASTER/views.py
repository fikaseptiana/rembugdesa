from django.shortcuts import render
from rest_framework import viewsets

<<<<<<< HEAD
from MASTER.models import Kabupaten, Kecamatan ,Kelurahan, Provinsi, Dusun
from MASTER.serializers import KecamatanSerializer, KelurahanSerializer, KabupatenSerializer, ProvinsiSerializer, \
    DusunSerializer
=======
from MASTER.models import Kabupaten, Kecamatan ,Kelurahan, Provinsi, Dusun, Peralatan
from MASTER.serializers import KecamatanSerializer, KelurahanSerializer, KabupatenSerializer, ProvinsiSerializer, \
    DusunSerializer, PeralatanSerializer
>>>>>>> 58d9661c466c7b4de1d8096096fb78de7020e426


class ProvinsiViewSet(viewsets.ModelViewSet):
    queryset = Provinsi.objects.all()
    serializer_class = ProvinsiSerializer


class KabupatenViewSet(viewsets.ModelViewSet):
    queryset = Kabupaten.objects.all()
    serializer_class = KabupatenSerializer


class KecamatanViewSet(viewsets.ModelViewSet):
    queryset = Kecamatan.objects.all()
    serializer_class = KecamatanSerializer


class KelurahanViewSet(viewsets.ModelViewSet):
    queryset = Kelurahan.objects.all()
    serializer_class = KelurahanSerializer

class DusunViewSet(viewsets.ModelViewSet):
    queryset = Dusun.objects.all()
    serializer_class = DusunSerializer
<<<<<<< HEAD
=======


class PeralatanViewSe(viewsets.ModelViewSet):
    queryset = Peralatan.objects.all()
    serializer_class = PeralatanSerializer
>>>>>>> 58d9661c466c7b4de1d8096096fb78de7020e426
