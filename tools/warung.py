import main

def start():
    while True:
        print("Ini warung mini")
        play_again = input("Kembali ke menu utama? [y/g] ")
        
        if play_again == "y":
            main.menu()
    
    
if __name__ == '__main__':
    start()