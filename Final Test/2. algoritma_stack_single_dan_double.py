#Nama : William Okta Jaya
#NIM : D0425510
#Prodi : Sistem Informasi clas b
#Matkul : Algoritma dan struktur data ( UAS )

#Contoh algoritma stack single dan double

#algoritma stack single

stack = []

# PUSH (menambah data)
stack.append("william")
stack.append("sistem informasi")

# POP (mengambil data)
hasil = stack.pop()

print("Yang diambil:", hasil)
print("Sisa stack:", stack)

#algoritma stack double

stack1 = []
stack2 = []

# Operasi pada Stack 1
stack1.append("william") # jika ini dihapus maka akan hilang namun jika ditambah akan muncul soalnya dia menghapus bagian awal
stack1.append("teknik")
stack1.pop()

# Operasi pada Stack 2
stack2.append("sistem informasi")
stack2.pop()

print("nama :", stack1)
print("fakultas :", stack2)
