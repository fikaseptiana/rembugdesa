from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Kabupaten, Kecamatan, Kelurahan, KecamatanResource, KelurahanResource, KabupatenResource, Provinsi, ProvinsiResource, \
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
