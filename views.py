from os import system

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

def tentang apl():
	system("cls")
	print("""
	*********************
	APLIKASI KONTAK SUPER
	*********************
		""")
	input("Tekan ENTER untuk kembali ke MENU UTAMA")