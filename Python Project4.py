sayur = ['bayam', 'kangkung', 'wortel', 'selada']


def tambahSayur() :
    sayurTambahan = input("Masukkan nama sayur yang ingin ditambahkan : ")
    
    sayur.append(sayurTambahan)
    return sayur

def hapusSayur() :
    sayurHilang = input("Masukkan nama sayur yang ingin dihapus : ")

    sayur.remove(sayurHilang)
    return sayur

def readSayur() :
    print(sayur)


print("Apa yang program bisa lakukan untukmu : ")
print("A. Tambah data sayur")
print("B. Hapus data sayur")
print("C. Tampilkan data sayur")
print("0. Keluar")

i = True
while(i == True) :
    print()
    opsi = input("Pilihan Anda : ")

    if(opsi=='A' or opsi=='a') :
            tambahSayur()
            
    elif(opsi=='B' or opsi=='b') :
            hapusSayur()

    elif(opsi=='C' or opsi=='c') :
            readSayur()

    elif(opsi=='0') :
        break
    
    else :
            print('Inputan Invalid')
            continue

