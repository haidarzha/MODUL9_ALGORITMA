def tulis_biodata():
    nama = input("Masukkan Namamu: ")
    umur = input("Masukkan Umurmu: ")
    alamat = input("Masukkan Alamatmu: ")
    email = input("Masukkan Emailmu: ")
    dosen_wali = input("Masukkan Nama Dosen Walimu: ")
    with open("Biodata.txt", "w") as file:
        file.write(f"Nama: {nama}\n")
        file.write(f"Umur: {umur}\n")
        file.write(f"Alamat: {alamat}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Dosen Wali: {dosen_wali}\n")

def baca_biodata():
    try:
        with open("Biodata.txt", "r") as file:
            print("\nBerikut ini data kamu:")
            print(file.read())
    except FileNotFoundError:
        print("File Biodata.txt tidak ditemukan. Pastikan untuk menulis biodata terlebih dahulu.")

tulis_biodata()
baca_biodata()
