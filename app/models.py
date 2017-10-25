from django.db import models
import os
import random
from django.utils import timezone
from django.contrib.auth.models import User, Group


def content_file_name(instance, filename):
    now = timezone.now()
    x = str(now).replace("-", "").replace(" ", "").replace(":",  "").replace("+", "").replace(".", "")
    ext = filename.split('.')[-1]
    name = random.randint(100, 99999)
    filename = "%s%s.%s" % (x, name, ext)
    return os.path.join(filename)


class Khoa(models.Model):
	ma_khoa = models.CharField(max_length=255, blank=True, null=True)
	ten_khoa = models.CharField(max_length=255, blank=True, null=True)
	updated_by = models.ForeignKey(User, related_name='khoa_updated_by', editable=True, null=True)
	created_by = models.ForeignKey(User, related_name='khoa_created_by', editable=True, null=True)
	created = models.DateTimeField(auto_now_add = True, auto_now = False, null=True)
	updated = models.DateTimeField(auto_now_add = True, auto_now = False, null=True)

	def __str__(self):
		return u'%s' % self.ma_khoa


class KhoaHoc(models.Model):
	ma_khoa_hoc = models.CharField(max_length=255, blank=True, null=True)
	ten_khoa_hoc = models.CharField(max_length=255, blank=True, null=True)
	updated_by = models.ForeignKey(User, related_name='khoa_hoc_updated_by', editable=True, null=True)
	created_by = models.ForeignKey(User, related_name='khoa_hoc_created_by', editable=True, null=True)
	created = models.DateTimeField(auto_now_add = True, auto_now = False, null=True)
	updated = models.DateTimeField(auto_now_add = True, auto_now = False, null=True)

	def __str__(self):
		return u'%s' % self.ma_khoa_hoc


class Khoa_KhoaHoc(models.Model):
	ma_khoa = models.ForeignKey(Khoa, related_name='tb_khoa')
	ma_khoa_hoc = models.ForeignKey(KhoaHoc, related_name='tb_khoa_hoc')

	def __str__(self):
		return u'%s' % self.ma_khoa


class GiangVien(models.Model):
	gioi_tinh = (
	    ("1", "Nam"),
	    ("0", "Nu"),
	)

	ma_giang_vien = models.CharField(max_length=255, blank=True, null=True)
	ten_giang_vien = models.CharField(max_length=255, blank=True, null=True)
	gioi_tinh = models.CharField(max_length=9, choices=gioi_tinh, default="1")
	so_dien_thoai = models.IntegerField(blank=True, null=True)
	email = models.EmailField(max_length=255, blank=True, null=True)
	ngay_sinh = models.DateField(null=True, blank=True)
	updated_by = models.ForeignKey(User, related_name='giang_vien_updated_by', editable=True, null=True)
	created_by = models.ForeignKey(User, related_name='giang_vien_created_by', editable=True, null=True)
	created = models.DateTimeField(auto_now_add = True, auto_now = False, null=True)
	updated = models.DateTimeField(auto_now_add = True, auto_now = False, null=True)

	def __str__(self):
		return u'%s' % self.ma_giang_vien


class Lop(models.Model):
	ma_lop = models.CharField(max_length=255, blank=True, null=True)
	ten_lop = models.CharField(max_length=255, blank=True, null=True)
	ma_khoa_hoc = models.ForeignKey(KhoaHoc, related_name="lop_kho_hoc", null=True)
	updated_by = models.ForeignKey(User, related_name='lop_updated_by', editable=True, null=True)
	created_by = models.ForeignKey(User, related_name='lop_created_by', editable=True, null=True)
	created = models.DateTimeField(auto_now_add = True, auto_now = False, null=True)
	updated = models.DateTimeField(auto_now_add = True, auto_now = False, null=True)

	def __str__(self):
		return u'%s' % self.ma_lop


class SinhVien(models.Model):
	gioi_tinh = (
	    ("1", "Nam"),
	    ("0", "Nu"),
	)

	ma_sinh_vien = models.CharField(max_length=255, blank=True, null=True)
	ten_sinh_vien = models.CharField(max_length=255, blank=True, null=True)
	user = models.ForeignKey(User, related_name='sinh_vien_user', null=True)
	gioi_tinh = models.CharField(max_length=9, choices=gioi_tinh, default="1")
	so_dien_thoai = models.IntegerField(blank=True, null=True)
	email = models.EmailField(max_length=255, blank=True, null=True)
	ngay_sinh = models.DateField(null=True, blank=True)
	ma_lop = models.ForeignKey(Lop, related_name='sinh_vien_lop', null=True)
	updated_by = models.ForeignKey(User, related_name='sinh_vien_updated_by', editable=True, null=True)
	created_by = models.ForeignKey(User, related_name='sinh_vien_created_by', editable=True, null=True)
	created = models.DateTimeField(auto_now_add = True, auto_now = False, null=True)
	updated = models.DateTimeField(auto_now_add = True, auto_now = False, null=True)

	def __str__(self):
		return u'%s' % self.ma_sinh_vien


class MonHoc(models.Model):
	ma_hoc_phan = models.CharField(max_length=255, blank=True, null=True)
	ten_hoc_phan = models.CharField(max_length=255, blank=True, null=True)
	gioi_han = models.IntegerField(default=0)
	da_dang_ky = models.IntegerField(default=0)
	so_tin_chi = models.IntegerField(default=0)
	ma_giang_vien = models.ForeignKey(GiangVien, related_name='giang_vien_mon_hoc', null=True, blank=True)
	ma_khoa_hoc = models.ForeignKey(KhoaHoc, related_name='khoa_hoc_mon_hoc', null=True, blank=True)
	ma_khoa = models.ForeignKey(Khoa, related_name='khoa_mon_hoc', null=True, blank=True)
	updated_by = models.ForeignKey(User, related_name='mon_hoc_updated_by', editable=True, null=True)
	created_by = models.ForeignKey(User, related_name='mon_hoc_created_by', editable=True, null=True)
	created = models.DateTimeField(auto_now_add = True, auto_now = False, null=True)
	updated = models.DateTimeField(auto_now_add = True, auto_now = False, null=True)

	def __str__(self):
		return u'%s' % self.ma_hoc_phan


class SinhVien_MonHoc(models.Model):
	ma_sinh_vien = models.ForeignKey(SinhVien, related_name='sinh_vien', null=True, blank=True)
	ma_hoc_phan = models.ForeignKey(MonHoc, related_name='mon_hoc', null=True, blank=True)
	active = models.BooleanField(default=False)

	def __str__(self):
		return u'%s' % self.ma_hoc_phan

