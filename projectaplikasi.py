from os import system
import sys

def print_menu():
	system("cls")
	menu_tampilan = """
	**********************
	PENDAFTARAN SISWA BARU
	**********************
	[A]. Informasi Siswa
	[B]. Lihat Semua Siswa
	[C]. Cari Siswa
	[D]. batalkan siswa
	[E]. Edit Informasi Siswa
	[F]. Tentang Pendaftaran
	[G]. Keluar Pendaftaran
	"""
	print(menu_tampilan)

def informasi_siswa():
	system("cls")
	print("Menambahkan Siswa Baru\nInformasi Siswa")
	nama = input("Nama\t:")
	telp = input("Telp\t:")
	ortu = input("Ortu\t:")
	sekolah = input("Sekolah\t:")
	respon = input(f"Yakin ingin menyimpan {nama} ? (Y/N) ")
	if respon.upper() == "Y":
		students[nama] = {
			"telp" : telp,
			"ortu" : ortu,
			"sekolah" : sekolah
		}
		print("Informasi Siswa Tersimpan.")
	else:
		print("Batal menyimpan.")
	input("Tekan ENTER untuk kembali ke MENU")

def lihat_semua_siswa():
	system("cls")
	print("Daftar Siswa Baru Yang Telah Disimpan")
	if len(students) == 0:
		print("Belum ada data yg disimpan saat ini.")
	else:
		print("NAMA |\t |NOMOR TELEPON|\t |ORTU|\t |SEKOLAH")
		for student in students:
			print(student,"|\t|", students[student]["telp"],"|\t|", students[student]["ortu"],"|\t|", students[student]["sekolah"])
	input("Tekan ENTER untuk kembali ke MENU")

def cari_siswa(student):
	if student in students:
		print("- RESULT -")
		print("Nama :",student)
		print("Telp :",students[student]["telp"])
		print("Ortu :",students[student]["ortu"])
		print("Sekolah :",students[student]["sekolah"])
		return True
	else:
		print("informasi tidak ditemukan.")
		return False

def tampilan_cari_siswa():
	system("cls")
	print("Pencarian Siswa")
	nama = input("Nama Siswa yang dicari : ")
	cari_siswa(nama)
	input("Tekan ENTER untuk kembali ke MENU")


def batalkan_siswa():
	system("cls")
	print("Batalkan  Pendaftaran Siswa")
	nama = input("Nama  yang ingin dibatalkan : ")
	result = cari_siswa(nama)
	if result:
		respon = input("Yakin dihapus (Y/N) : ")
		if respon.upper() == "Y":
			del students[nama]
			print(f"siswa {nama} telah dibatalkan.")
		else:
			print(f"Batalkan pendaftaran siswa {nama}")
	input("Tekan ENTER untuk kembali ke MENU")

def edit_telp_siswa(student):
	print("INFORMASI YANG AKAN DIPERBARUI")
	print("DATA LAMA")
	print(f"Telp\t:{students[student]['telp']}")
	new_telp = input("Masukkan Nomor Telp Baru : ")
	students[student]["telp"] = new_telp
	print("Data berhasil diperbarui")
	cari_siswa(student)

def edit_ortu_siswa(student):
	pass

def edit_sekolah_siswa(student):
	pass

def edit_nama_kontak(student):
	print("INFORMASI YANG AKAN DIPERBARUI")
	print("DATA LAMA")
	print(f"Nama\t:{students}")
	new_nama = input("Masukkan Nama Baru : ")
	#copy data lama ke kontak baru,yang lama hapus.
	student[new_nama] = students[student]
	del students[student]
	print("Data berhasil diperbarui")
	cari_siswa(new_nama)

def edit_info():
	system("cls")
	print("EDIT INFO SISWA")
	nama = input("Nama Siswa yang akan di edit infonya : ")
	result = cari_siswa(nama)
	if result:
		print("EDIT [1]NAMA, [2]TELP, [3]ORTU, [4]SEKOLAH")
		respon = input("Pilihan Informasi yg akan diedit (1/2/3/4) : ")
		if respon == "1":
			pass
		elif respon == "2":
			edit_telp_siswa(nama)
		elif respon == "3":
			edit_ortu_siswa(nama)
		elif respon == "4":
			pass
	input("Tekan ENTER untuk kembali ke MENU")

def cek_respon_user(char):
	if char == "A":
		informasi_siswa()
	elif char == "B":
		lihat_semua_siswa()
	elif char == "C":
		tampilan_cari_siswa()
	elif char == "D":
		batalkan_siswa()
	elif char == "E":
		edit_info()
	elif char == "F":
		pass
	elif char == "G":
		pass
	else:
		print("INVALID RESPON")
		input("Enter to Back ...")

students = {
	'Alvin' : {
		'telp' : '0822',
		'ortu' : 'abdul',
		'sekolah' : 'xaverius'
	},
	'Budi' : {
		'telp' : '0812',
		'ortu' : 'kadet',
		'sekolah' : 'kumbang'
	}
}
user_respon = ""
while user_respon != "G":
	print_menu()
	user_respon = input("RESPON : ").upper()
	cek_respon_user(user_respon)
else:
	system("cls")
	print("Good Bye....")
	#sys.exit()
