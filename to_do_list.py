
"Todo list PY"
"""
Program To-Do List Sederhana
Fitur: tambah tugas, lihat tugas, tandai selesai, hapus tugas, keluar
Data disimpan sementara di memori (hilang kalau program ditutup)
"""
 
def tampilkan_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Tambah tugas")
    print("2. Lihat tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Keluar")
 
 
def tampilkan_tugas(daftar_tugas):
    if not daftar_tugas:
        print("\nBelum ada tugas.")
        return
 
    print("\n--- Daftar Tugas ---")
    for i, tugas in enumerate(daftar_tugas, start=1):
        status = "✓" if tugas["selesai"] else " "
        print(f"[{status}] {i}. {tugas['nama']}")
 
 
def main():
    daftar_tugas = []
 
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")
 
        if pilihan == "1":
            nama_tugas = input("Masukkan nama tugas: ")
            daftar_tugas.append({"nama": nama_tugas, "selesai": False})
            print(f"Tugas '{nama_tugas}' berhasil ditambahkan.")
 
        elif pilihan == "2":
            tampilkan_tugas(daftar_tugas)
 
        elif pilihan == "3":
            tampilkan_tugas(daftar_tugas)
            if daftar_tugas:
                try:
                    nomor = int(input("Nomor tugas yang selesai: "))
                    daftar_tugas[nomor - 1]["selesai"] = True
                    print("Tugas ditandai selesai.")
                except (ValueError, IndexError):
                    print("Nomor tidak valid.")
 
        elif pilihan == "4":
            tampilkan_tugas(daftar_tugas)
            if daftar_tugas:
                try:
                    nomor = int(input("Nomor tugas yang mau dihapus: "))
                    tugas_terhapus = daftar_tugas.pop(nomor - 1)
                    print(f"Tugas '{tugas_terhapus['nama']}' dihapus.")
                except (ValueError, IndexError):
                    print("Nomor tidak valid.")
 
        elif pilihan == "5":
            print("Sampai jumpa!")
            break
 
        else:
            print("Pilihan tidak valid, coba lagi.")
 
 
if __name__ == "__main__":
    main()
 
