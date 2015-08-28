from django.db import models
from import_export import resources
<<<<<<< HEAD
from MASTER.models import KegiatanResource, AnggotaResource, DusunResource
=======

>>>>>>> a40b157b433c1d18b815faac65a4bc3103722e32


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

<<<<<<< HEAD
class JadwalResource(resources.ModelResource):
=======
classJadwalResource(resources.ModelResource):
>>>>>>> a40b157b433c1d18b815faac65a4bc3103722e32
    class Meta:
        model = Jadwal

# Create your models here.
