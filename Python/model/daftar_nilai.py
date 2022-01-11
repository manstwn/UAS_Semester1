from view.input_nilai import *

tabelsiswa = {}

def tambah():
    print("\n")
    print("Menambahkan Data Mahasiswa")
    nim = input_nim()
    nama = input_nama()
    tugas = input_tugas()
    uts = input_uts()
    uas = input_uas()
    akhir = input_akhir()
    tabelsiswa[nim] = [nim, nama, tugas, uts, uas, akhir]
    print("Data telah berhasil diinput!")
    print("\n")
        

def ubah():
    print("\n")
    print("Mengubah Data Mahasiswa")
    nim = input("Masukkan NIM \t: ")
    if nim in tabelsiswa.keys():
        print("Data dengan NIM {} ditemukan, silakan masukan perubahan.".format(nim))
        tabelsiswa[nim][1] = input("Masukan Perubahan Nama\t: ")
        tabelsiswa[nim][2] = int(input("Masukan Perubahan Nilai Tugas\t: "))
        tabelsiswa[nim][3] = int(input("Masukan Perubahan Nilai UTS\t: "))
        tabelsiswa[nim][4] = int(input("Masukan Perubahan Nilai UAS\t: "))
        tabelsiswa[nim][5] = tabelsiswa[nim][2] *.3 + tabelsiswa[nim][3] *.35 + tabelsiswa[nim][4] *.35
        print("Data behasil diubah!")
    else:
        print("'{}' Tidak ditemukan.".format(nim))
    print("\n")


def hapus():
    print("\n")
    print("Menghapus Data Mahasiswa")
    nim = input("Masukan NIM \t: ")
    if nim in tabelsiswa.keys():
        del tabelsiswa[nim]
        print("Berhasil menghapus data dengan NIM '{}'".format(nim))
    else:
        print("Data dengan NIM '{}' tidak ditemukan.".format(nim))

def mencari():
    print("\n")
    print("Mencari Data Mahasiswa")
    nim = input("Masukan NIM\t: ")
    if nim in tabelsiswa.keys():
        print("="*68)
        print("|    NIM    |      Nama      | Tugas |  UTS  |  UAS  | Akhir |")
        print("="*68)
        print("| {0:9} | {1:14} | {2:5} | {3:5} | {4:5} | {5:5}".format(nim, tabelsiswa[nim][1], tabelsiswa[nim][2], tabelsiswa[nim][3], tabelsiswa[nim][4], tabelsiswa[nim][5]))
        print("-"*68)
    else:
        print("Data dengan NIM '{}' tidak ditemukan.".format(nim))
    print("\n")
