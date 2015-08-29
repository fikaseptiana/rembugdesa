from django.db import models
from import_export import resources
<<<<<<< HEAD
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
=======
from MASTER.models import Dusun, Jeniskegiatan, Repeatable, Kependudukan

class Kegiatan(models.Model):
    id_jensikegiatan = models.ForeignKey(Jeniskegiatan)
    tanggal = models.CharField(max_length=100)
    tempat = models.CharField(max_length=100)
    id_anggota = models.ForeignKey(Kependudukan)
    contact = models.CharField(max_length=100)
    id_repeatable = models.ForeignKey(Repeatable)
    id_dusun = models.ForeignKey(Dusun)

>>>>>>> 58d9661c466c7b4de1d8096096fb78de7020e426

    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __unicode__(self):
<<<<<<< HEAD
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
=======
        return self.id_jensikegiatan

class KegiatanResource(resources.ModelResource):
    class Meta:
        model = Kegiatan
        
class AnggotakegiatanResource(models.Model):
    id_kegiatan = models.ForeignKey(Kegiatan)
    id_anggota = models.ForeignKey(Kependudukan)
    kehadiran = models.CharField(max_length=100)

    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.id_anggota


class AnggotakegiatanResource(resources.ModelResource):
    class Meta:
        model = Anggotakegiatan
>>>>>>> 58d9661c466c7b4de1d8096096fb78de7020e426
