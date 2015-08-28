from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from MASTER.views import KabupatenViewSet, KecamatanViewSet, KelurahanViewSet, DusunViewSet, ProvinsiViewSet, \
        KegiatanViewSet, AnggotaViewSet, PerlengkapanViewSet, JadwalViewSet

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'provinsis', ProvinsiViewSet)
router.register(r'kabupatens', KabupatenViewSet)
router.register(r'kecamatans', KecamatanViewSet)
router.register(r'dusuns', DusunViewSet)
router.register(r'kegiatans', KegiatanViewSet)
router.register(r'anggotas', AnggotaViewSet)
router.register(r'perlengkapans', PerlengkapanViewSet)
router.register(r'jadwals', JadwalViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'REMBUGDESA.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
]
