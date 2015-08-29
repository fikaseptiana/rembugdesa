__author__ = 'Pamungkas Jayuda'

from rest_framework import serializers

<<<<<<< HEAD
from MASTER.models import Kecamatan, Kelurahan, Kabupaten, Provinsi, Dusun

=======
from MASTER.models import Kecamatan, Kelurahan, Kabupaten, Provinsi, Dusun, Peralatan
>>>>>>> 58d9661c466c7b4de1d8096096fb78de7020e426

class ProvinsiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provinsi
        fields = (
            'nama_provinsi',
            'keterangan'
        )

class KabupatenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kabupaten
        fields = (
            'nama_kabupaten',
            'keterangan'
        )


class KecamatanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kecamatan
        fields = (
            'nama_kabupaten',
            'nama_kecamatan',
            'keterangan'
        )

class KelurahanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kelurahan
        fields = (
            'nama_kecamatan',
            'nama_kelurahan',
            'keterangan'
        )


class DusunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dusun
        fields = (
            'nama_kelurahan',
            'nama_dusun',
            'keterangan'
        )
<<<<<<< HEAD
=======

class PeralatanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Peralatan
        fields = (
            'nama_peralatan'
        )
>>>>>>> 58d9661c466c7b4de1d8096096fb78de7020e426
