def buat_file(nama_file):
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    tahun_angkatan = input("Masukkan tahun angkatan: ")
    
    with open(nama_file, 'w') as file:
        file.write(f"Nama: {nama}\n")
        file.write(f"NIM: {nim}\n")
        file.write(f"Tahun Angkatan: {tahun_angkatan}\n")
    print(f"File {nama_file} telah dibuat dengan data diri.")

def baca_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            print(f"Isi file {nama_file}:")
            print(file.read())
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")

def tambah_isi_file(nama_file, data):
    with open(nama_file, 'a') as file:
        file.write(data + '\n')
    print(f"Data telah ditambahkan ke dalam file {nama_file}.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Membuat dan Menulis file")
        print("2. Membaca file")
        print("3. Menambahkan text pada file")
        print("4. Keluar dari Program")
        pilihan = input("Masukkan Pilihan Berupa Angka (1/2/3/4): ")

        if pilihan == '1':
            nama_file = input("Masukkan nama file: ")
            buat_file(nama_file)
        
        elif pilihan == '2':
            nama_file = input("Masukkan nama file yang ingin dibaca: ")
            baca_file(nama_file)
        
        elif pilihan == '3':
            nama_file = input("Masukkan nama file untuk ditambah data: ")
            data = input("Masukkan data yang ingin ditambahkan: ")
            tambah_isi_file(nama_file, data)
        
        elif pilihan == '4':
            print("Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu()