from django.db import models
from import_export import resources
from MASTER.models import KegiatanResource, AnggotaResource, DusunResource


class Jadwal(models.Model):
    jeniskegiatan = models.ForeignKey(Kegiatan)
    tanggal = models.CharField(max_length=100)
    tempat = models.CharField(max_length=100)
    pic = models.ForeignKey(Anggota)
    contact = models.CharField(max_length=100)
    anggota =models.ForeignKey(Anggota)
    repeateble = models.CharField(max_length=100)
    dusun = models.ForeignKey(Dusun)

    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.jeniskegiatan

class JadwalResource(resources.ModelResource):
    class Meta:
        model = Jadwal

# Create your models here.
