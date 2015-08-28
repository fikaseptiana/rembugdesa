from django.shortcuts import render
from rest_framework import viewsets

from MASTER.models import Kabupaten, Kecamatan ,Kelurahan, Provinsi, Dusun, Kegiatan, Anggota, Perlengkapan
from MASTER.serializers import KecamatanSerializer, KelurahanSerializer, KabupatenSerializer, ProvinsiSerializer, \
    DusunSerializer, KegiatanSerializer, AnggotaSerializer, PerlengkapanSerializer


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

class KegiatanViewSet(viewsets.ModelViewSet):
    queryset = Kegiatan.objects.all()
    serializer_class = KegiatanSerializer

class AnggotaViewSet(viewsets.ModelViewSet):
    queryset = Anggota.objects.all()
    serializer_class = AnggotaSerializer

class PerlengkapanViewSet(viewsets.ModelViewSet):
    queryset = Perlengkapan.objects.all()
    serializer_class = PerlengkapanSerializer
