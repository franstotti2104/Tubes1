nasabah_dic_umum = {}
lst_nasabah = []
saldo_nasabah_dict = {}
id_nasabah = ""
saldo = 0

def id_maker(nama, no_hp):
    if(len(nama.split()) > 1):
        nama = nama.split()[0]
    id_final = 0
    for char in nama:
        id_raw = ord(char)
        id_final += id_raw
    
    id_final = id_final//10

    id = f"{nama}-{no_hp}-{id_final}"
    return id

def registrasi():
    nama = input("Masukkan nama Anda: ")
    no_hp = input("Masukkan nomor HP Anda: ")
    password = input("Masukkan password Anda: ")
    lst_nasabah.append(id_maker(nama.upper(), no_hp))
    nasabah_dic_umum[id_maker(nama.upper(), no_hp)] = password
    saldo_nasabah_dict[id_maker(nama.upper(), no_hp)] = 0
    id = print(f"ID Anda: {id_maker(nama.upper(),no_hp)}")
    return id, nasabah_dic_umum, lst_nasabah

def cek_nasabah():
    id_nasabah = input("Masukkan ID Anda: ")
    if(id_nasabah in lst_nasabah):
        print("ID Anda tercatat di sistem kami.")
    else:
        print("ID Anda belum ada di sistem kami.")
        print("Silahkan Registrasi untuk menikmati penawaran kami.")

def cek_saldo(id_nasabah):
    return saldo_nasabah_dict[id_nasabah]
    

def setor_tunai(banyak_setoran, id_nasabah):
    saldo_nasabah_dict[id_nasabah] += banyak_setoran
    return saldo_nasabah_dict[id_nasabah]

def tarik_tunai(banyak_tarik, id_nasabah):
    if(saldo_nasabah_dict[id_nasabah] == 0):
        print("Maaf saat ini Saldo Anda sebesar 0, Mohon lakukan Setor Tunai!")
    elif(saldo_nasabah_dict[id_nasabah]<banyak_tarik):
        print("Maaf saldo Anda tidak cukup, Mohon lakukan Setor Tunai!")
        print(f"Saldo Anda: {saldo_nasabah_dict[id_nasabah]}")
    else:
        saldo_nasabah_dict[id_nasabah] -= banyak_tarik
        print("Tarik Tunai berhasil!")
        print(f"Saldo Anda: {saldo_nasabah_dict[id_nasabah]}")

def transfer(id_nasabah, id_dituju, besar_transfer):
    if(saldo_nasabah_dict[id_nasabah] < besar_transfer):
        print("Maaf Saldo Anda tidak cukup, Mohon lakukan Setor Tunai!")
    else:
        saldo_nasabah_dict[id_nasabah] -= besar_transfer
        saldo_nasabah_dict[id_dituju] += besar_transfer
        print("Transfer Berhasil!")
        print(f"Saldo Anda: {saldo_nasabah_dict[id_nasabah]}")
    

def login():
    while True:
        print("ID: ")
        id_nasabah = input()
        print("Password: ")
        password_nasabah = input()
        if(id_nasabah not in lst_nasabah):
            print("ID atau Password salah, silahkan coba kembali.")
            print()
        elif(nasabah_dic_umum[id_nasabah] != password_nasabah):
            print("ID atau Password salah, silahkan coba kembali.")
            print()
        else:
            nama = id_nasabah.split("-")[0]
            print(f"Selamat datang {nama.capitalize()}")
            break
    while True:
        menu_login()
        pilihan_menu = int(input("Pilihan menu Anda: "))
        if(pilihan_menu == 1):
            print("==============================")
            print(f"Saldo Anda: {cek_saldo(id_nasabah)}")
            print("==============================")
        elif(pilihan_menu == 2):
            print("==============================")
            banyak_setoran = int(input("Masukkan jumlah setor tunai: "))
            print("Setor Tunai Berhasil!")
            print(f"Saldo Anda: {setor_tunai(banyak_setoran, id_nasabah)}")
            print("==============================")
        elif(pilihan_menu == 3):
            print("==============================")
            banyak_tarik = int(input("Masukkan jumlah yang ingin Anda tarik: "))
            tarik_tunai(banyak_tarik, id_nasabah)
            print("==============================")
        elif(pilihan_menu == 4):
            print("==============================")
            print("Mohon maaf, saat ini kami tidak menyediakan transfer antar bank")
            print("Kami hanya menyediakan transfer antar sesama pengguna STEI-ATM")
            while True:
                id_dituju = input("Masukkan ID Nasabah yang ingin Anda tuju: ")
                if(id_dituju not in lst_nasabah):
                    print("ID tidak ditemukan")
                else:
                    break
            besar_transfer = int(input("Masukkan nominal transfer Anda: "))
            transfer(id_nasabah, id_dituju, besar_transfer)
            print("==============================")
        elif(pilihan_menu == 0):
            print("==============================")
            print(f"Terima kasih telah menggunakan layanan kami {nama.capitalize()}.")
            print("==============================")
            break
        

        

def menu_login():
    print("============MENU==============")
    print("1. Cek Saldo")
    print("2. Setor Tunai")
    print("3. Tarik Tunai")
    print("4. Transfer")
    print("0. Exit")
    


while True:
    print("Selamat datang di STEI-ATM")
    print("============MENU==============")
    print("1. Registrasi")
    print("2. Cek Nasabah")
    print("3. Login")
    print("0. Exit")
    menu = int(input("Pilihan menu anda: "))
    if(menu == 0):
        print("Terima kasih telah menggunakan STEI-ATM")
        break
    elif(menu == 1):
        print("==============================")
        registrasi()
        print("==============================")
    elif(menu == 2):
        print("==============================")
        cek_nasabah()
        print("==============================") 
    elif(menu == 3):
        print("==============================")
        login()
        print("==============================")
    elif(menu == 0):
        print("==============================")
        print("Terima kasih telah menggunakan STEI-ATM!")
        print("==============================")
        break