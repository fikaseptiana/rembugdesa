from django.db import models
from import_export import resources

class Kegiatan(models.Model):
    id_jensikegiatan = models.ForeignKey(Jeniskegiatan)
    tanggal = models.CharField(max_length=100)
    tempat = models.CharField(max_length=100)
    id_anggota = models.ForeignKey(Kependudukan)
    contact = models.CharField(max_length=100)
    id_repeatable = models.ForeignKey(Repeatable)
    id_dusun = models.ForeignKey(Dusun)


    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.id_jensikegiatan

class KegiatanResource(resources.ModelResource):
    class Meta:
        model = Kegiatan
