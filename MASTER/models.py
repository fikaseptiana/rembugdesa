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


class Kegiatan(models.Model):
    posyandu = models.CharField(max_length=100)
    arisan = models.CharField(max_length=100)
    kerjabakti = models.CharField(max_length=100)

    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.posyandu


class KegiatanResource(resources.ModelResource):
    class Meta:
        model = Kegiatan


class Anggota(models.Model):
    id_anggota = models.CharField(max_length=100)
    nama_anggota = models.CharField(max_length=100)
    hadir = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=500)

    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.nama_anggota


class AnggotaResource(resources.ModelResource):
    class Meta:
        model = Anggota

class Perlengkapan(models.Model):
    pic = models.ForeignKey(Anggota)
    item = models.CharField(max_length=100)
    qty = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=500)

    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.item


class PerlengkapanResource(resources.ModelResource):
    class Meta:
        model = Perlengkapan
