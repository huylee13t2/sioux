from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    # url(r'^api/invite$', views.invite, name='invite'),
    # url(r'^api/get-user$', views.get_user, name='get_user'),
    # # user
    # url(r'^api/register$', views.register, name='register'),
    url(r'^api/dang-nhap$', views.login, name='login'),
    url(r'^api/danh-sach-mon-hoc$', views.list_all, name='list_all'),
    url(r'^api/danh-sach-da-chon$', views.danh_sach_da_chon, name='danh_sach_da_chon'),
    url(r'^api/thong-tin-mon-hoc$', views.thong_tin_mon_hoc, name='thong_tin_mon_hoc'),
    url(r'^api/dang-ky-mon-hoc$', views.dang_ky, name='dang_ky'),
    url(r'^api/huy-dang-ky-mon-hoc$', views.huy_dang_ky, name='huy_dang_ky'),
    url(r'^api/danh-sach-da-dang-ky$', views.danh_sach_da_dang_ky, name='danh_sach_da_dang_ky'),
]

