from django.shortcuts import render
from rest_framework import viewsets

from MASTER.models import Kabupaten, Kecamatan ,Kelurahan, Provinsi, Dusun,  Peralatan
from MASTER.serializers import KecamatanSerializer, KelurahanSerializer, KabupatenSerializer, ProvinsiSerializer, DusunSerializer, JeniskegiatanSerializer, RepeatableSerializers

from TRANSAKSI.models import Anggotakegiatan, Kegiatan, Kependudukan, Jeniskegiatan, Repeatable
from TRANSAKSI.serializers import AnggotakegiatanSerializer, KegiatanSerializer, KependudukanSerializers, JeniskegiatanSerializer, RepeatableSerializer

class KegiatanlViewSet(viewsets.ModelViewSet):
    queryset = Kegiatan.objects.all()
    serializer_class= KegiatanSerializer


class AnggotakegiatanViewSet(viewsets.ModelViewSet):
    queryset = Anggotakegiatan.objects.all()
    serializer_class = AnggotakegiatanSerializer
