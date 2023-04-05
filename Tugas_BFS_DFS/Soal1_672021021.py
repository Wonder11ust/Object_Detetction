import sys


def Kasir():
    pesanan = input("masukkan pesanan:")
    harga = input("masukkan harga barang:")
    harga = int(harga)
    jumlah = input("masukkan jumlah yang ingin dibeli:")
    jumlah = int(jumlah)
    total1 = harga *jumlah
    total = print(pesanan,",=",total1)
    pembayaran = int(input("Masukkan pembayaran:"))
    kembalian = pembayaran-total1
    if pembayaran<total1:
        print("maaf uang anda tidak cukup uang anda kurang ",total1-pembayaran)
        ulangi = input("ingin ulangi pembayaran?(y/n)")
        if ulangi == "y":
            Kasir()
        else:
            menu()
    else:
        print("kembalian anda ",kembalian)
        ulangi1 = input("ingin ulangi program kasir?(y/n)")
        if ulangi1 == "y":
            Kasir()
        else:
            menu()


def pascal_triangle():
    n = int(input("Masukkan ukuran segitiga Pascal: "))

    # Inisialisasi segitiga Pascal
    triangle = [[1]]

    # Buat baris-baris berikutnya
    for i in range(1, n):
        # Buat baris baru dengan satu di awal
        row = [1]

        # Tambahkan angka-angka dari baris sebelumnya
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # Tambahkan satu di akhir
        row.append(1)

        # Tambahkan baris baru ke segitiga Pascal
        triangle.append(row)

    # Cetak segitiga Pascal
    for row in triangle:
        print(" ".join(str(num) for num in row).center(n * 3))
    ulangi = input("Ingin kembali ke menu?(y/n)")
    if ulangi == "y":
        menu()
    else:
        pascal_triangle()
    return triangle





def menu():
    checker = {1,2,3}
    print("===MAIN MENU APLIKASI KASIR===")
    print("selamat datang di aplikasi kasir")
    print("===masukkan input aplikasi kasir===")

    print("1.Porgram Kasir")
    print("2.Segitiga")
    print("3.Exit")
    while True:
        pilihan = int(input("masukkan pilihan:"))
        while pilihan<=2 and pilihan >=1:
            if pilihan == 1:
                Kasir()
                break;
            elif pilihan == 2:
                pascal_triangle();


                break;
        while pilihan >2:
            break;
        while pilihan <1:
            break;
        while pilihan == 3:
            sys.exit("Program exit")


username = "672021021"
password = "672021021"
print("Halaman login kasir")
username1 = input("Masukkan username kasir:")
password1 = input("masukkan password:")
if(username == username1 and password == password1):
    print("login berhasil.....")
    menu()

else:
   print("username/password salah silahkan ulang program")