from django.shortcuts import render
from rest_framework import viewsets

from MASTER.models import Kabupaten, Kecamatan ,Kelurahan, Provinsi, Dusun, Anggotakegiatan, Peralatan, Kegiatan
from MASTER.serializers import KecamatanSerializer, KelurahanSerializer, KabupatenSerializer, ProvinsiSerializer, \
    DusunSerializer, AnggotakegiatanSerializer, ProvinsiSerializer, KegiatanSerializer


class KegiatanlViewSet(viewsets.ModelViewSet):
    queryset = Kegiatan.objects.all()
    serializer_class= KegiatanSerializer


class AnggotakegiatanViewSet(viewsets.ModelViewSet):
    queryset = Anggotakegiatan.objects.all()
    serializer_class = AnggotakegiatanSerializer
