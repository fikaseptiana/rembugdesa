from django.db import models
from import_export import resources



class Provinsi(models.Model):
    nama_provinsi = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=500)

    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.nama_provinsi

class ProvinsiResource(resources.ModelResource):
    class Meta:
        model = Provinsi


class Kabupaten(models.Model):
    id_provinsi = models.ForeignKey(Provinsi)
    nama_kabupaten = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=500)

    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.nama_kabupaten

class KabupatenResource(resources.ModelResource):
    class Meta:
        model = Kabupaten


class Kecamatan(models.Model):
    id_kabupaten = models.ForeignKey(Kabupaten)
    nama_kecamatan = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=500)

    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.nama_kecamatan


class KecamatanResource(resources.ModelResource):
    class Meta:
        model = Kecamatan


class Kelurahan(models.Model):
    id_kecamatan = models.ForeignKey(Kecamatan)
    nama_kelurahan = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=500)

    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.nama_kelurahan


class KelurahanResource(resources.ModelResource):
    class Meta:
        model = Kelurahan


class Dusun(models.Model):
    id_kelurahan = models.ForeignKey(Kelurahan)
    nama_dusun = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=500)

    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.nama_dusun


class DusunResource(resources.ModelResource):
    class Meta:
        model = Dusun
<<<<<<< HEAD
=======



class Peralatan(models.Model):
    nama_peralatan = models.CharField(max_length=100)


    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.nama_peralatan


class PeralatanResource(resources.ModelResource):
    class Meta:
        model = Peralatan
>>>>>>> 58d9661c466c7b4de1d8096096fb78de7020e426
