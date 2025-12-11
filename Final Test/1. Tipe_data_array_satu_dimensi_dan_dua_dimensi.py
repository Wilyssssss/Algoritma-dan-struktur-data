#Nama : William Okta Jaya
#NIM : D0425510
#Prodi : Sistem Informasi
#Matkul : Algoritma dan struktur data ( UAS )

#Contoh tipe data aray satu dimensi

nama_alamat_umur = ["William Okta Jaya","desa sumberjo",19]
print (nama_alamat_umur)

#Contoh tipe data array dua dimensi

nama_alamat_umur_dan_makanan = [
    ["william okta jaya", "desa sumberjo", 19],
    ["apel", "anggur", "jambu"],
    ["pelem", "semangka", "rambutan"]
]

# Print untuk seluruh
print(nama_alamat_umur_dan_makanan)

# Print per baris
for baris in nama_alamat_umur_dan_makanan:
    print(baris)

#Contoh tipe data array tiga dimensi

nama_teman2_kelasB = [
    [
        ["william", "alim"],
        ['mahmud', "naufal"]
    ],
    [
        ["sandry", "irsan"],
        ["jona", "masriadi"]
    ]
]
print(nama_teman2_kelasB)