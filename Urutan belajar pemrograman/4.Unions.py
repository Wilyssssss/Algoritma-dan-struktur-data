#Nama : William Okta Jaya
#NIM : D0425510
#Prodi : Sistem Informasi / Class B
#Mata kuliah : Algoritma dan struktur data (Pak Muzaki)

#1.4 Konsep Unions : 

#unions dapat memiliki dua makna utama, yaitu:
	
#Unions pada himpunan (set union) untuk menggabungkan dua atau lebih data.
#Unions pada tipe data (Union Type Hint) untuk menyatakan bahwa suatu variabel bisa memiliki lebih dari satu tipe data.

#1.) Konsep Union pada Himpunan (Set Union)
#Union pada set adalah operasi untuk menggabungkan dua atau lebih himpunan dan menghilangkan data yang sama. Hasilnya adalah semua elemen unik dari seluruh set yang digabungkan.

A = {1, 2, 3}
B = {3, 4, 5}

C = A.union(B)
print(C)

#2.) Konsep Union pada Tipe Data (Union Type Hint)
#Union juga digunakan dalam type hint untuk menyatakan bahwa suatu variabel dapat memiliki lebih dari satu tipe data. Ini digunakan untuk membantu keterbacaan dan pemeriksaan tipe dalam program.

#Contoh menggunakan Union dari typing:

from typing import Union

data: Union[int, float]
data = 10
data = 10.5

#Artinya, variabel data boleh bertipe int atau float.

#Contoh fungsi dengan Union:
	
from typing import Union

def cetak(data: Union[int, str]):
    print(data)

cetak(10)
cetak("Halo")
