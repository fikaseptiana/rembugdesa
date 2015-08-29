from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from MASTER.views import KabupatenViewSet, KecamatanViewSet, KelurahanViewSet, DusunViewSet, ProvinsiViewSet
<<<<<<< HEAD
from TRANSAKSI.views import JeniskegiatanViewSet, RepeatableViewSet, PerlengkapankegiatanViewSet
=======
from TRANSAKSI.views import KegiatanViewSet,  AnggotakegiatanViewSet
>>>>>>> 58d9661c466c7b4de1d8096096fb78de7020e426

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'provinsis', ProvinsiViewSet)
router.register(r'kabupatens', KabupatenViewSet)
router.register(r'kecamatans', KecamatanViewSet)
router.register(r'dusuns', DusunViewSet)
<<<<<<< HEAD
router.register(r'jeniskegiatans', JeniskegiatanViewSet)
router.register(r'repeatable', RepeatableViewSet)
router.register(r'perlengkapankegiatans', PerlengkapankegiatanViewSet)
=======
router.register(r'anggotakegiatan', AnggotakegiatanViewSet)
router.register(r'peralatan', PeralatanViewSet)
router.register(r'kegiatan', KegiatanViewSet)

>>>>>>> 58d9661c466c7b4de1d8096096fb78de7020e426
urlpatterns = [
    # Examples:
    # url(r'^$', 'REMBUGDESA.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
]
