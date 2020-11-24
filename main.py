from os import system

import views
from Models import user

user_respon = ""
while user_respon != "G":
	views.print_menu()	
	user_respon = input("RESPON : ").upper()
	user.cek_respon_user(user_respon)
else:
	system("cls")
	print("Good Bye....")
	