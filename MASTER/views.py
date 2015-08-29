from django.shortcuts import render
from rest_framework import viewsets

from MASTER.models import Kabupaten, Kecamatan ,Kelurahan, Provinsi, Dusun, Anggotakegiatan, Peralatan
from MASTER.serializers import KecamatanSerializer, KelurahanSerializer, KabupatenSerializer, ProvinsiSerializer, \
    DusunSerializer, AnggotakegiatanSerializer, PeralatanSerializer


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

class AnggotakegiatanViewSet(viewsets.ModelViewSet):
    queryset = Anggotakegiatan.objects.all()
    serializer_class = AnggotakegiatanSerializer

class PeralatanViewSe(viewsets.ModelViewSet):
    queryset = Peralatan.objects.all()
    serializer_class = PeralatanSerializer
