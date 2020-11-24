from os import system
from json import load, dump

students = none

def load_students():
	with open("student_table.json", "r") as file:
		students = load(file)
def save_students():
	global students
	with open("students_table.json", "w") as file:
		dump(students, file)

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
		save_students()
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
	input("Tekan ENTER untuk kembali ke MENU"

def edit_telp_siswa(student):
	print("INFORMASI YANG AKAN DIPERBARUI")
	print("DATA LAMA")
	print(f"Telp\t:{students[student]['telp']}")
	new_telp = input("Masukkan Nomor Telp Baru : ")
	students[student]["telp"] = new_telp
	print("Data berhasil diperbarui")
	cari_siswa(student)
	save_students

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


def load_students():
	with open("models/student_table.json", "r") as file:
		students = load(file)
def save_students():
	with open("students_table.json", "w") as file:
		dump(students, file)

students = none
