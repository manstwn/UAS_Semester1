def input_nim():
    global nim
    nim = input("Masukan NIM\t: ")
    return nim

def input_nama():
    global nama
    nama = input("Masukan Nama\t: ")
    return nama

def input_tugas():
    global tugas
    tugas = int(input("Masukan nilai Tugas\t: "))
    return tugas

def input_uts():
    global uts
    uts = int(input("Masukan nilai UTS\t: "))
    return uts

def input_uas():
    global uas
    uas = int(input("Masukan nilai UAS\t: "))
    return uas

def input_akhir():
    global akhir
    akhir = (tugas *.3 + uts *.35 + uas * .35)
    return akhir
