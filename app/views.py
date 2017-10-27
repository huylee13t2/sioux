from django.shortcuts import render
from django.db.models import Q
import json
from django.http import *
from django.views.decorators.csrf import csrf_exempt
# import jwt
from django.contrib.auth.models import User, Group

from app.models import Khoa, KhoaHoc, Khoa_KhoaHoc, GiangVien, Lop, SinhVien, MonHoc, SinhVien_MonHoc


def main(req):
	return render(req, 'index.html', {})

# account
@csrf_exempt
def login(request):
	username = request.POST.get('ma_sinh_vien')
	password = request.POST.get('mat_khau')

	try:
		sinh_vien = SinhVien.objects.get(user__username = username)
		
		if sinh_vien.user.check_password(password):
			lop = Lop.objects.get(ma_lop = sinh_vien.ma_lop)
			khoa_hoc = KhoaHoc.objects.get(ma_khoa_hoc = lop.ma_khoa_hoc)
			khoa = Khoa.objects.get(ma_khoa = lop.ma_khoa)

			response = {
				'result' : 1,
				'data' : {
					'id' : sinh_vien.user.id,
					'username' : sinh_vien.user.username,
					'email' : sinh_vien.email,
					'ma_sinh_vien' : sinh_vien.ma_sinh_vien,
					'ten_sinh_vien' : sinh_vien.ten_sinh_vien,
					'gioi_tinh' : sinh_vien.gioi_tinh,
					'so_dien_thoai' : sinh_vien.so_dien_thoai,
					'ngay_sinh' : sinh_vien.ngay_sinh,
					'ma_lop' : lop.ma_lop,
					'ten_lop' : lop.ten_lop,
					'ma_khoa_hoc' : khoa_hoc.ma_khoa_hoc,
					'ten_khoa_hoc' : khoa_hoc.ten_khoa_hoc,
					'updated' : sinh_vien.updated,
					'ma_khoa' : khoa.ma_khoa,
					'ten_khoa' : khoa.ten_khoa,
				}
			}
		else:
			response = {
				'result' : 0,
			}
	except:
		response = {
			'result' : -999,
		}

	return JsonResponse(response)


# danh sach cac mon dang ky

@csrf_exempt
def list_all(req):
	username = req.POST.get('ma_sinh_vien')

	try:
		sinh_vien = SinhVien.objects.get(user__username = username)
		lop = Lop.objects.get(ma_lop = sinh_vien.ma_lop)
		khoa_hoc = KhoaHoc.objects.get(ma_khoa_hoc = lop.ma_khoa_hoc)
		khoa = Khoa.objects.get(ma_khoa = lop.ma_khoa)
		
		mon_hoc = MonHoc.objects.filter(Q(ma_khoa = lop.ma_khoa) & Q(ma_khoa_hoc = lop.ma_khoa_hoc))

		list_mon_hoc = []

		for obj in mon_hoc:
			giang_vien = GiangVien.objects.get(ma_giang_vien = obj.ma_giang_vien)

			list_mon_hoc.append({
				'id' : obj.id,
				'ma_hoc_phan' : obj.ma_hoc_phan,
				'ten_hoc_phan' : obj.ten_hoc_phan,
				'gioi_han' : obj.gioi_han,
				'da_dang_ky' : obj.da_dang_ky,
				'so_tin_chi' : obj.so_tin_chi,
				'ma_giang_vien' : giang_vien.ma_giang_vien,
				'ten_giang_vien' : giang_vien.ten_giang_vien,
				'updated' : obj.updated,
			})

		response = {
			'result' : 1,
			'data' : list_mon_hoc
		}
	

	except:
		response = {
			'result' : -999
		}

	return JsonResponse(response)

# danh sach cac mon da chon dang ky
@csrf_exempt
def danh_sach_da_chon(req):

	ma_sinh_vien = req.POST.get('ma_sinh_vien')

	try:
		sinh_vien = SinhVien.objects.get(ma_sinh_vien = ma_sinh_vien)

		sinh_vien_mon_hoc = SinhVien_MonHoc.objects.filter(Q(ma_sinh_vien = sinh_vien) & Q(active = False))

		list_mon_hoc = []
		for obj in sinh_vien_mon_hoc:
			mon_hoc = MonHoc.objects.get(ma_hoc_phan = obj.ma_hoc_phan)
			giang_vien = GiangVien.objects.get(ma_giang_vien = mon_hoc.ma_giang_vien)

			list_mon_hoc.append({
				'id' : mon_hoc.id,
				'ma_hoc_phan' : mon_hoc.ma_hoc_phan,
				'ten_hoc_phan' : mon_hoc.ten_hoc_phan,
				'gioi_han' : mon_hoc.gioi_han,
				'da_dang_ky' : mon_hoc.da_dang_ky,
				'so_tin_chi' : mon_hoc.so_tin_chi,
				'ma_giang_vien' : giang_vien.ma_giang_vien,
				'ten_giang_vien' : giang_vien.ten_giang_vien,
			})

		response = {
			'result' : 1,
			'data' : list_mon_hoc
		}

	except:
		response = {
			'result' : -999,
		}

	return JsonResponse(response)


# thogn tin mon hoc
@csrf_exempt
def thong_tin_mon_hoc(req):

	# username = req.POST.get('ma_sinh_vien')
	ma_hoc_phan = req.GET.get('ma_hoc_phan')

	try:
		mon_hoc = MonHoc.objects.get(ma_hoc_phan = ma_hoc_phan)
		giang_vien = GiangVien.objects.get(ma_giang_vien = mon_hoc.ma_giang_vien)

		response = {
			'result' : mon_hoc.id,
			'data' : {
				'id' : mon_hoc.id,
				'ma_hoc_phan' : mon_hoc.ma_hoc_phan,
				'ten_hoc_phan' : mon_hoc.ten_hoc_phan,
				'gioi_han' : mon_hoc.gioi_han,
				'da_dang_ky' : mon_hoc.da_dang_ky,
				'so_tin_chi' : mon_hoc.so_tin_chi,
				'ma_giang_vien' : obj.ma_giang_vien,
				'ten_giang_vien' : giang_vien.ten_giang_vien,
			}
		}

	except:
		response = {
			'result' : -999
		}

	return JsonResponse(response)

# dang ky mon hoc
@csrf_exempt
def dang_ky(req):

	username = req.POST.get('ma_sinh_vien')
	ma_hoc_phan = req.POST.get('ma_hoc_phan')

	try:
		sinh_vien = SinhVien.objects.get(ma_sinh_vien = ma_sinh_vien)
		mon_hoc = MonHoc.objects.get(ma_hoc_phan = ma_hoc_phan)

		obj = SinhVien_MonHoc(ma_sinh_vien = sinh_vien.ma_sinh_vien, ma_hoc_phan=mon_hoc.ma_hoc_phan)
		obj.save()

		response = {
			'result' : obj.id,
		}

	except:
		response = {
			'result' : -999
		}

	return JsonResponse(response)


@csrf_exempt
def huy_dang_ky(req):

	username = req.POST.get('ma_sinh_vien')
	ma_hoc_phan = req.POST.get('ma_hoc_phan')

	try:
		sinh_vien = SinhVien.objects.get(ma_sinh_vien = ma_sinh_vien)
		mon_hoc = MonHoc.objects.get(ma_hoc_phan = ma_hoc_phan)

		obj = SinhVien_MonHoc.objects.filter(Q(ma_sinh_vien=sinh_vien.ma_sinh_vien) & Q(ma_hoc_phan=mon_hoc.ma_hoc_phan))

		if(obj.length > 0):
			obj.delete()

			response = {
				'result' : 1,
			}
		else:
			response = {
				'result' : 0
			}
	except:

		response = {
			'result' : -999
		}

	return JsonResponse(response)

@csrf_exempt
def danh_sach_da_dang_ky(req):

	username = req.POST.get('ma_sinh_vien')

	try:
		sinh_vien = SinhVien.objects.get(user__username = username)
		sinh_vien_mon_hoc = SinhVien_MonHoc.objects.filter(Q(ma_sinh_vien = sinh_vien.ma_sinh_vien) & Q(active = True))

		list_mon_hoc = []
		for obj in sinh_vien_mon_hoc:
			mon_hoc = MonHoc.objects.get(ma_hoc_phan = obj.ma_hoc_phan)
			giang_vien = GiangVien.objects.get(ma_giang_vien = mon_hoc.ma_giang_vien)

			list_mon_hoc.append({
				'id' : mon_hoc.id,
				'ma_hoc_phan' : mon_hoc.ma_hoc_phan,
				'ten_hoc_phan' : mon_hoc.ten_hoc_phan,
				'gioi_han' : mon_hoc.gioi_han,
				'da_dang_ky' : mon_hoc.da_dang_ky,
				'so_tin_chi' : mon_hoc.so_tin_chi,
				'ma_giang_vien' : giang_vien.ma_giang_vien,
				'ten_giang_vien' : giang_vien.ten_giang_vien,
			})

		response = {
			'result' : 1,
			'data' : list_mon_hoc
		}

	except:
		response = {
			'result' : -999,
		}

	return JsonResponse(response)