#Nama : William Okta Jaya
#NIM : D0425510
#Prodi : Sistem Informasi / Class B
#Mata kuliah : Algoritma dan struktur data (Pak Muzaki)

#1.3 Konsep struktur : 

#1.) Struktur sekuensial
# Struktur sekuensial adalah alur program yang dijalankan secara berurutan dari atas ke bawah, tanpa ada percabangan atau pengulangan.

# Ciri utama: Perintah dieksekusi satu per satu sesuai urutan penulisan. 
#contoh :
	
print("Masukkan nama:")
nama = input()
print("Halo", nama)

#2.) Struktur seleksi (Percabangan)
#Struktur seleksi digunakan untuk mengambil keputusan berdasarkan suatu kondisi. Jika kondisi benar, maka perintah tertentu dijalankan, jika salah dijalankan perintah lain.

#Bentuk umum:
#if
#if–else
#if–elif–else 

#contoh :
nilai = 75

if nilai >= 70:
    print("Lulus")
else:
    print("Tidak Lulus")

#3.) Struktur Perulangan (Looping)
#Struktur perulangan digunakan untuk mengulang perintah yang sama beberapa kali selama syarat tertentu terpenuhi.
#Jenis perulangan:
#for
#while

#contoh :
for i in range(1, 6):
    print(i)

#4.) Struktur Modular (Fungsi / Prosedur)
#Struktur modular digunakan untuk memecah program besar menjadi bagian-bagian kecil (fungsi) agar program lebih rapi, mudah dibaca, dan mudah diperbaiki.

#contoh :
def sapa():
    print("Halo, selamat datang")

sapa()

#5.) Struktur Data (Pendukung Struktur Program)
# Struktur pemrograman sering dipadukan dengan struktur data untuk menyimpan dan mengolah data, seperti: Variabel,Array / List,Dictionary,Tuple

#contoh :
nilai = [80, 85, 90]
