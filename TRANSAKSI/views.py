from django.shortcuts import render
from rest_framework import viewsets

from MASTER.models import Kabupaten, Kecamatan ,Kelurahan, Provinsi, Dusun
from MASTER.serializers import KecamatanSerializer, KelurahanSerializer, KabupatenSerializer, ProvinsiSerializer, \
    DusunSerializer


class JadwalViewSet(viewsets.ModelViewSet):
    queryset = Jadwal.objects.all()
    serializer_class= JadwalSerializer
