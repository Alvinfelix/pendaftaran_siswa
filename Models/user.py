from . import contact


def cek_respon_user(char):
	if char == "A":
		contact.informasi_siswa()
	elif char == "B":
		contact.lihat_semua_siswa()
	elif char == "C":
		contact.tampilan_cari_siswa()
	elif char == "D":
		contact.batalkan_siswa()
	elif char == "E":
		contact.edit_info()
	elif char == "F":
		pass
	elif char == "G":
		pass
	else:
		print("INVALID RESPON")
		input("Enter to Back ...")