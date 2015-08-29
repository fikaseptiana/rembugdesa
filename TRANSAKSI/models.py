from django.db import models
from import_export import resources
from MASTER.models import Dusun, Peralatan
from TRANSAKSI.models import Anggota, Kegiatan


class Jeniskegiatan(models.Model):
    nama_jeniskegiatan = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=100)

    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __unicode__(self):
        return self.nama_jeniskegiatan

class Repeatable(models.Model):
    nama_repeatable = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=100)

    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __unicode__(self):
        return self.nama_repeatable




class Perlengkapankegiatan(models.Model):
    id_kegiatan = models.ForeignKey(kegiatan)
    id_peralatan = models.ForeignKey(peralatan)
    qty = models.CharField(max_length=100)
    pic = models.ForeignKey(anggota)
    keterangan = models.CharField(max_length=500)

    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.id_peralatan
