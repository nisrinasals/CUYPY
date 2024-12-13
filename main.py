import random
from libs import welcome_message

# cuypy_position = random.randint(1, 4)
welcome_message("HALO, SELAMAT DATANG DI CUYPY GAMES!")

nama_user = input("Masukkan nama kamu: ")

while nama_user == "":
    nama_user = input("isi nama dulu: ")

# bentuk_goa = "|_|"
# goa_kosong = [bentuk_goa] * 4 # HARUS KOSONG

# goa = goa_kosong.copy() # TEMPAT CUYPY
# goa[cuypy_position -1] = "|0_0|"

# goa_kosong = ' '.join(goa_kosong)
# goa = ' '.join(goa)

while True:

    cuypy_position = random.randint(1, 4)
    
    bentuk_goa = "|_|"
    goa_kosong = [bentuk_goa] * 4 # HARUS KOSONG
 
    goa = goa_kosong.copy() # TEMPAT CUYPY
    goa[cuypy_position -1] = "|0_0|"

    goa_kosong = ' '.join(goa_kosong)
    goa = ' '.join(goa)

    print(f"\n\nHalo, {nama_user}!  Coba lihat goa dibawah ini \n {goa_kosong}\n")

    pilihan_user = int(input("Menurutmu CUYPY di goa nomor berapa? [1 / 2 / 3 / 4]: "))

    # while pilihan_user != 1|2|3|4:
    #     pilihan_user = int(input("Masukkan angka antara 1 sampai 4: "))

    # while pilihan_user == "":
    #     pilihan_user = int(input("Masukkan angka antara 1 sampai 4: "))

    konfirmasi = input(f"Yakin pilih {pilihan_user} [y/g]?")
    if konfirmasi == "g":
        print("Program dihentikan")
        exit()
    elif konfirmasi == "y":
        if pilihan_user == cuypy_position:
            print(f"\nUhuyy, selamat {nama_user}, kamu menang! CUYPY ada di {cuypy_position} dan kamu pilih nomor {pilihan_user}🥳. \n {goa}")
        else:
            print(f"\nYahhh, kamu kalah! CUYPY bukan disitu, tapi di goa nomor {cuypy_position} dan kamu pilih goa nomor {pilihan_user}.🙂‍↔️ \n {goa}")
    else:
        print("Pilihan ga ada cuy. Ulangi programnya")
        exit()
        
    play_again = input("\nMau lanjut main? [y/g]")
    if play_again == "g":
        break
    
print("\nOke, trims sudah bermain")