from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Kabupaten, Kecamatan, Kelurahan, KecamatanResource, KelurahanResource, KabupatenResource, Provinsi, ProvinsiResource, \
<<<<<<< HEAD
    DusunResource, Dusun, Kegiatan, KegiatanResource, Peralatan, PeralatanResource


class JeniskegiatanAdmin(ImportExportModelAdmin):
    list_display = ['nama_jeniskegiatan', 'keterangan']
    resource_class = JeniskegiatanResource
    pass

admin.site.register(Jeniskegiatan, JeniskegiatanAdmin)

class RepeatableAdmin(ImportExportModelAdmin):
    list_display = ['nama_repeatable', 'keterangan']
    resource_class = RepeatableResource
    pass

admin.site.register(Repeatable, RepeatableAdmin)

class PerlengkapankegiatanAdmin(ImportExportModelAdmin):
    list_display = ['id_kegiatan','id_peralatan', 'keterangan']
    resource_class = PerlengkapankegiatanResource
    pass

admin.site.register(Perlengkapankegiatan, PerlengkapankegiatanAdmin)
=======
    Anggotakegiatan, AnggotakegiatanResource, Kegiatan, KegiatanResource, Jeniskegiatan, JeniskegiatanResource, Kependudukan, KependudukanResource, \
    Repeatable, RepeatableResource



class KegiatanAdmin(ImportExportModelAdmin):
    list_display = ['id_jensikegiatan', 'tanggal', 'tempat', 'id_anggota', 'contact', 'id_repeatable', 'id_dusun']
    resource_class = KegiatanResource
    pass

admin.site.register(Kegiatan, KegiatanAdmin)

class AnggotakegiatanAdmin(ImportExportModelAdmin):
    list_display = ['id_kegiatan', 'id_anggota', 'kehadiran']
    resource_class = AnggotakegiatanResource
    pass

admin.site.register(Anggotakegiatan, AnggotakegiatanAdmin)
>>>>>>> 58d9661c466c7b4de1d8096096fb78de7020e426
