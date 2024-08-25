def menu_utama():
    print("==============================")
    print("=   MENU MANAJEMEN TUGAS     =")
    print("==============================")
    print("= (1) Tambah Tugas Baru      =")
    print("= (2) Hapus Tugas            =")
    print("= (3) Perbarui Status Tugas  =")
    print("= (4) Cari Tugas             =")
    print("= (5) Tampilkan Daftar Tugas =")
    print("==============================")
    try:
        opsi = int(input("Masukkan Pilihan: "))
        pilih_opsi(opsi)
    except ValueError:
        print("Masukkan harus berupa angka.")
        menu_utama()

def pilih_opsi(opsi):
    if opsi == 1:
        tambah_tugas()
    elif opsi == 2:
        hapus_tugas()
    elif opsi == 3:
        perbarui_status_tugas()
    elif opsi == 4:
        cari_tugas()
    elif opsi == 5:
        tampilkan_daftar_tugas()
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang sesuai.")
        menu_utama()
daftar_tugas = []

def tambah_tugas():
    print("Tambah Tugas Baru")
    print("=================")
    judul = input("Masukkan judul tugas: ")
    deadline = input("Masukkan deadline tugas (DD/MM/YYYY): ")
    daftar_tugas.append({'judul': judul, 'deadline': deadline, 'selesai': False})
    print("Tugas telah ditambahkan.")
    kembali_ke_menu()

def hapus_tugas():
    print("Hapus Tugas")
    print("===========")
    judul = input("Masukkan judul tugas yang akan dihapus: ")
    for tugas in daftar_tugas:
        if tugas['judul'] == judul:
            daftar_tugas.remove(tugas)
            print("Tugas telah dihapus.")
            kembali_ke_menu()
    print("Tidak ada tugas dengan judul tersebut.")
    kembali_ke_menu()

def perbarui_status_tugas():
    print("Perbarui Status Tugas")
    print("=====================")
    judul = input("Masukkan judul tugas yang statusnya akan diperbarui: ")
    for tugas in daftar_tugas:
        if tugas['judul'] == judul:
            tugas['selesai'] = not tugas['selesai']
            print("Status tugas berhasil diperbarui.")
            kembali_ke_menu()
    print("Tidak ada tugas dengan judul tersebut.")
    kembali_ke_menu()

def cari_tugas():
    print("Cari Tugas")
    print("==========")
    judul = input("Masukkan judul tugas yang ingin dicari: ")
    found = False
    for tugas in daftar_tugas:
        if tugas['judul'] == judul:
            print("Tugas ditemukan:")
            print("Judul:", tugas['judul'])
            print("Deadline:", tugas['deadline'])
            print("Status:", "Selesai" if tugas['selesai'] else "Belum selesai")
            found = True
            break
    if not found:
        print("Tidak ada tugas dengan judul tersebut.")
    kembali_ke_menu()

def tampilkan_daftar_tugas():
    print("Daftar Tugas")
    print("============")
    if not daftar_tugas:
        print("Tidak ada tugas dalam daftar.")
    else:
        for i, tugas in enumerate(daftar_tugas, start=1):
            print(f"{i}. Judul: {tugas['judul']}, Deadline: {tugas['deadline']}, Status: {'Selesai' if tugas['selesai'] else 'Belum selesai'}")
    kembali_ke_menu()

def kembali_ke_menu():
    opsi = input('\nApakah Anda ingin kembali ke menu utama? (Y/N): ')
    if opsi.lower() == 'y':
        menu_utama()

# Menjalankan program
menu_utama()
