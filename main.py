import random

welcome_massage = "WELCOME TO CUYPY GAMES!"
cuypy_position = random.randint(1, 4)

print("*****************************")
print(f"** {welcome_massage} **")
print("*****************************")

nama_user = input("Masukkan nama kamu: ")

print(f'''
Halo, {nama_user}! Coba perhatikan goa dibawah ini
        |_|     |_|     |_|     |_| 
''')

pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: "))

konfirmasi = input(f"Apakah kamu yakin akan memilih {pilihan_user} [y/n]?")
if konfirmasi == "n":
    exit()
    
if pilihan_user == cuypy_position:
    print(f"Selamat {nama_user}, kamu menang! posisi CUYPY ada di {cuypy_position} dan pilihanmu adalah {pilihan_user}.")
else:
    print(f"KAMU KALAH! CUYPY bukan berada disitu, tapi ada di goa nomor {cuypy_position}. Sedangkan kamu memilih goa nomor {pilihan_user}.")