from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Kabupaten, Kecamatan, Kelurahan, KecamatanResource, KelurahanResource, KabupatenResource, Provinsi, ProvinsiResource, \
    DusunResource, Dusun
from TRANSAKSI.models import Jadwal

class JadwalAdmin(ImportExportModelAdmin):
    list_display = ['jenis_kegiatan', 'tanggal', 'tempat', 'pic', 'contact', 'anggota', 'repeatable', 'dusun']
    resource_class = JadwalResource
    pass

admin.site.register(Jadwal, JadwalAdmin)
