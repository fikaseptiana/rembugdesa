from django.shortcuts import render
from rest_framework import viewsets

<<<<<<< HEAD
from MASTER.models import Kabupaten, Kecamatan ,Kelurahan, Provinsi, Dusun
from TRANSAKSI.serializers import Kegiatan, Peralatan
=======
from MASTER.models import Kabupaten, Kecamatan ,Kelurahan, Provinsi, Dusun,  Peralatan
from MASTER.serializers import KecamatanSerializer, KelurahanSerializer, KabupatenSerializer, ProvinsiSerializer, DusunSerializer, JeniskegiatanSerializer, RepeatableSerializers
>>>>>>> 58d9661c466c7b4de1d8096096fb78de7020e426

from TRANSAKSI.models import Anggotakegiatan, Kegiatan, Kependudukan, Jeniskegiatan, Repeatable
from TRANSAKSI.serializers import AnggotakegiatanSerializer, KegiatanSerializer, KependudukanSerializers, JeniskegiatanSerializer, RepeatableSerializer

<<<<<<< HEAD
class JeniskegiatanViewSet(viewsets.ModelViewSet):
    queryset = Jeniskegiatan.objects.all()
    serializer_class = ProvinsiSerializer


class RepeatableViewSet(viewsets.ModelViewSet):
    queryset = Repeatable.objects.all()
    serializer_class = RepeatableSerializer


class PerlengkapankegiatanViewSet(viewsets.ModelViewSet):
    queryset = Perlengkapankegiatan.objects.all()
    serializer_class = PerlengkapankegiatanSerializer
=======
class KegiatanlViewSet(viewsets.ModelViewSet):
    queryset = Kegiatan.objects.all()
    serializer_class= KegiatanSerializer


class AnggotakegiatanViewSet(viewsets.ModelViewSet):
    queryset = Anggotakegiatan.objects.all()
    serializer_class = AnggotakegiatanSerializer
>>>>>>> 58d9661c466c7b4de1d8096096fb78de7020e426
