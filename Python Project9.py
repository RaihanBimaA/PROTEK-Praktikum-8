buah = {'apel' : 5000,
           'jeruk' : 8500,
           'mangga' : 7800,
           'duku' : 6500}

def jumlahBuah() :
    
    jumlah = int(input("Berapa Kg : "))
        
    print("-------------------------------------------")
    print("Total Harga : ", buah.get(namaBuah, 0)*jumlah)


namaBuah = input("Nama buah yang dibeli : ")

try:
    
    if(namaBuah in buah.keys()) :
        jumlahBuah()
        
    else :
        print("Maaf, buah yang anda masukkan tidak ada")

except ValueError :
    print("Silahkan jumlah buah dengan benar")
    jumlahBuah()
