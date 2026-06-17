import csv


# Membaca data dari CSV
def load_data():
    data = []

    with open("main.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    return data


# Menyimpan data ke CSV
def save_data(data):

    with open("main.csv", "w", newline="") as file:

        fieldnames = ["kode", "nama", "kategori", "stok", "harga"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for item in data:
            writer.writerow(item)


# ======== CREATE =========
def tambah_barang():

    data = load_data()

    kode = input("Kode barang : ").strip().upper()
    nama = input("Nama barang : ").strip().title()
    kategori = input("Kategori : ").strip().title()
    stok = input("Stok : ").strip()
    harga = input("Harga : ").strip()

    barang = {
        "kode": kode,
        "nama": nama,
        "kategori": kategori,
        "stok": stok,
        "harga": harga
    }

    data.append(barang)

    save_data(data)

    print("Data berhasil ditambahkan")


# ======== READ =========
def tampilkan_barang():   #function untuk menampilkan data barang

    data = load_data()

    print("\n===== DAFTAR BARANG =====")

    print(f"{'Kode':<8}{'Nama':<15}{'Kategori':<15}{'Stok':<10}{'Harga'}")

    for item in data:

        print(
            f"{item['kode']:<8}"
            f"{item['nama']:<15}"
            f"{item['kategori']:<15}"
            f"{item['stok']:<10}"
            f"{item['harga']}"
        )


# ======== SEARCH =========
def cari_barang():    #function untuk mencari data barang berdasarkan nama

    data = load_data()

    nama = input("Masukkan nama barang yang dicari : ").strip().lower() #strip digunakan untuk menghapus spasi di awal dan akhir input, lower() digunakan untuk mengubah input menjadi huruf kecil agar pencarian tidak case-sensitive

    ditemukan = False

    for item in data:

        if item["nama"].strip().lower() == nama:

            print("\nBarang ditemukan!")
            print("Kode     :", item["kode"])
            print("Nama     :", item["nama"])
            print("Kategori :", item["kategori"])
            print("Stok     :", item["stok"])
            print("Harga    :", item["harga"])

            ditemukan = True

            break

    if not ditemukan:
        print("Barang tidak ditemukan")


# ======== UPDATE =========
def update_barang():   #function untuk mengupdate data barang berdasarkan kode

    data = load_data()

    kode = input("Masukkan kode barang : ").strip().upper() #strip digunakan untuk menghapus spasi di awal dan akhir input, upper() digunakan untuk mengubah input menjadi huruf besar agar pencarian tidak case-sensitive

    ditemukan = False

    for item in data:

        if item["kode"].strip().upper() == kode:

            item["stok"] = input("Stok baru : ").strip()
            item["harga"] = input("Harga baru : ").strip()

            ditemukan = True

            break

    if ditemukan:

        save_data(data)

        print("Data berhasil diupdate")

    else:

        print("Barang tidak ditemukan")


# ======== DELETE =========
def hapus_barang():  #function untuk menghapus data barang berdasarkan kode

    data = load_data()

    kode = input("Masukkan kode barang : ").strip().upper() #strip digunakan untuk menghapus spasi di awal dan akhir input, upper() digunakan untuk mengubah input menjadi huruf besar agar pencarian tidak case-sensitive

    for item in data:

        if item["kode"].strip().upper() == kode:

            data.remove(item)

            save_data(data)

            print("Barang berhasil dihapus")

            return

    print("Barang tidak ditemukan")


# ======== SORTING =========
def urutkan_harga():    #function untuk mengurutkan data barang berdasarkan harga menggunakan algoritma bubble sort

    data = load_data()

    n = len(data)

    for i in range(n):

        for j in range(n - i - 1):

            if int(data[j]["harga"]) > int(data[j + 1]["harga"]):

                data[j], data[j + 1] = data[j + 1], data[j]

    print("\n=== Data Setelah Diurutkan ===")

    print(f"{'Kode':<8}{'Nama':<15}{'Kategori':<15}{'Stok':<10}{'Harga'}")

    for item in data:

        print(
            f"{item['kode']:<8}"
            f"{item['nama']:<15}"
            f"{item['kategori']:<15}"
            f"{item['stok']:<10}"
            f"{item['harga']}"
        )


# ======== MENU ==========
while True:

    print("""
===== SISTEM INVENTORI =====

1. Tambah Barang
2. Tampilkan Barang
3. Update Barang
4. Cari Barang
5. Hapus Barang
6. Urutkan Harga
7. Keluar
""")

    pilihan = input("Pilih menu : ").strip()

    if pilihan == "1":
        tambah_barang()

    elif pilihan == "2":
        tampilkan_barang()

    elif pilihan == "3":
        update_barang()

    elif pilihan == "4":
        cari_barang()

    elif pilihan == "5":
        hapus_barang()

    elif pilihan == "6":
        urutkan_harga()

    elif pilihan == "7":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")

