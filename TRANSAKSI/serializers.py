from rest_framework import serializers

from MASTER.models import  Kecamatan, Kelurahan, Kabupaten, Provinsi, Dusun
from TRANSAKSI.models import Kegiatan, Peralatan


class JeniskegiatanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jeniskegiatan
        fields = (
            'nama_jeniskegiatan',
            'keterangan'
        )

class RepeatableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Repeatable
        fields = (
            'nama_repeatable',
            'keterangan'
        )


class PerlengkapankegiatanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perlengkapankegiatan
        fields = (
            'id_kegiatan',
            'id_peralatan',
            'keterangan'
        )
