__author__ = 'Pamungkas Jayuda'

from rest_framework import serializers

from MASTER.models import Kecamatan, Kelurahan, Kabupaten, Provinsi, Dusun, Kegiatan, Anggota, Perlengkapan


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
class KegiatanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kegiatan
        fields = (
            'posyandu',
            'arisan',
            'kerjabakti'
        )

class AnggotaSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Anggota
            fields = (
            'id_anggota',
            'nama_anggota',
            'hadir',
            'keterangan'
                )


class PerlengkapanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perlengkapan
        fields = (
            'pic',
            'item',
            'qty',
            'keterangan'
        )
