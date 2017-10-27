from django.contrib import admin
from app.models import Khoa, KhoaHoc, Khoa_KhoaHoc, GiangVien, Lop, SinhVien, MonHoc, SinhVien_MonHoc

class KhoaAdmin(admin.ModelAdmin):
	list_display = ['ma_khoa', 'ten_khoa']

class KhoaHocAdmin(admin.ModelAdmin):
	list_display = ['ma_khoa_hoc', 'ten_khoa_hoc']

class Khoa_KhoaHocAdmin(admin.ModelAdmin):
	list_display = ['ma_khoa', 'ma_khoa_hoc']

class GiangVienAdmin(admin.ModelAdmin):
	list_display = ['ma_giang_vien', 'ten_giang_vien', 'gioi_tinh', 'so_dien_thoai', 'email', 'ngay_sinh']

class LopAdmin(admin.ModelAdmin):
	list_display = ['ma_lop', 'ten_lop', 'ma_khoa_hoc']

class SinhVienAdmin(admin.ModelAdmin):
	list_display = ['ma_sinh_vien', 'ten_sinh_vien', 'gioi_tinh', 'so_dien_thoai', 'email', 'ngay_sinh', 'ma_lop']

class MonHocAdmin(admin.ModelAdmin):
	list_display = ['ma_hoc_phan', 'ten_hoc_phan', 'gioi_han', 'da_dang_ky', 'so_tin_chi', 'ma_giang_vien', 'ma_khoa_hoc', 'ma_khoa']

class SinhVien_MonHocAdmin(admin.ModelAdmin):
	list_display = ['ma_sinh_vien', 'ma_hoc_phan','active']


admin.site.register(Khoa, KhoaAdmin)
admin.site.register(KhoaHoc, KhoaHocAdmin)
admin.site.register(Khoa_KhoaHoc, Khoa_KhoaHocAdmin)
admin.site.register(GiangVien, GiangVienAdmin)
admin.site.register(Lop, LopAdmin)
admin.site.register(SinhVien, SinhVienAdmin)
admin.site.register(MonHoc, MonHocAdmin)
admin.site.register(SinhVien_MonHoc, SinhVien_MonHocAdmin)