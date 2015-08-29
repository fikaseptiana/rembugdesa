from django.shortcuts import render
from rest_framework import viewsets

from MASTER.models import Kabupaten, Kecamatan ,Kelurahan, Provinsi, Dusun
from TRANSAKSI.serializers import Kegiatan, Peralatan


class JeniskegiatanViewSet(viewsets.ModelViewSet):
    queryset = Jeniskegiatan.objects.all()
    serializer_class = ProvinsiSerializer


class RepeatableViewSet(viewsets.ModelViewSet):
    queryset = Repeatable.objects.all()
    serializer_class = RepeatableSerializer


class PerlengkapankegiatanViewSet(viewsets.ModelViewSet):
    queryset = Perlengkapankegiatan.objects.all()
    serializer_class = PerlengkapankegiatanSerializer
