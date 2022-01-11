from model.daftar_nilai import tabelsiswa
def lihat():
    print("\n")
    if tabelsiswa.keys():
        no = 1
        for tabel in tabelsiswa.values():
            print("="*68)
            print("| No |    NIM    |      Nama      | Tugas |  UTS  |  UAS  | Akhir |")
            print("="*68)
            print("| {0:2} | {1:9} | {2:14} | {3:5} | {4:5} | {5:5} | {6:5}".format(no, tabel[0], tabel[1], tabel[2], tabel[3], tabel[4], tabel[5]))
            print("="*68)
            no += 1
    else :
        print("\n")
        print("Data tidak ditemukan")
        print("Mohon tambah data terlebih dahulu")
    print("\n")
