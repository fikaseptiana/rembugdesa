from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Kabupaten, Kecamatan, Kelurahan, KecamatanResource, KelurahanResource, KabupatenResource, Provinsi, ProvinsiResource, \
    Anggotakegiatan, AnggotakegiatanResource, Kegiatan, KegiatanResource

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
