from model.daftar_nilai import *
from view.view_nilai import *


while True:
    print("-"*30)
    print("Program Data Mahasiswa")
    print("-"*30)
    print("1. Tambah Data \n2. Tampilkan Data \n3. Ubah Data \n4. Hapus Data \n5. Cari Data \n0. Keluar")
    pilih = input("Masukkan pilihan Menu \t: ")
    if pilih == '1':
        tambah()

    elif pilih == '2':
        lihat()

    elif pilih == '3':
        ubah()

    elif pilih == '4':
        hapus()

    elif pilih == '5':
        mencari()

    elif pilih == '0':
        exit()

    else:
        print("pilihan salah")

