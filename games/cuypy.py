import random
import main

def start():
    while True:

        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4 # HARUS KOSONG
    
        cuypy_position = random.randint(1, 4)
    
        goa = goa_kosong.copy() # TEMPAT CUYPY
        goa[cuypy_position -1] = "|0_0|"

        goa_kosong = ' '.join(goa_kosong)
        goa = ' '.join(goa)

        print(f"\n\nCoba lihat goa dibawah ini \n {goa_kosong}\n")

        pilihan_user = int(input("Menurutmu CUYPY di goa nomor berapa? [1 / 2 / 3 / 4]: "))


        if pilihan_user == cuypy_position:
            print(f"\nUhuyy, selamat kamu menang! CUYPY ada di {cuypy_position} dan kamu pilih nomor {pilihan_user}🥳. \n {goa}")
        else:
            print(f"\nYahhh, kamu kalah! CUYPY bukan disitu, tapi di goa nomor {cuypy_position} dan kamu pilih goa nomor {pilihan_user}.🙂‍↔️ \n {goa}")

        play_again = input("\nMau lanjut main? [y/g]")
        if play_again == "g":
            main.menu()
        
    print("\nOke, trims sudah bermain")
    
if __name__ == '__main__':
    start()