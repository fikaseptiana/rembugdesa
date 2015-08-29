from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from MASTER.views import KabupatenViewSet, KecamatanViewSet, KelurahanViewSet, DusunViewSet, ProvinsiViewSet, \
        AnggotakegiatanViewSet, PerlengkapanViewSet, KegiatanViewSet
from TRANSAKSI.views import JadwalViewSet

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'provinsis', ProvinsiViewSet)
router.register(r'kabupatens', KabupatenViewSet)
router.register(r'kecamatans', KecamatanViewSet)
router.register(r'dusuns', DusunViewSet)
router.register(r'anggotaskegiatan', anggotaskegiatanViewSet)
router.register(r'Peralatan', PeralatanViewSet)
router.register(r'kegiatan', KegiatanViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'REMBUGDESA.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
]
