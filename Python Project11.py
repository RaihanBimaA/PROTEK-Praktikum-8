buah = {'apel' : 5000,
           'jeruk' : 8500,
           'mangga' : 7800,
           'duku' : 6500}

def jumlahBuah(namaBuah) :
    
    jumlah = int(input("Berapa Kg : ")) 
    harga = buah.get(namaBuah, 0)*jumlah
    return harga

def beliBuah() :
    try:

        total = []
        lanjut = True
        
        while(lanjut==True) :
            
            namaBuah = input("Nama buah yang dibeli : ")
            
            if(namaBuah in buah.keys()) :
                    
                    harga = jumlahBuah(namaBuah)
                    total.append(harga)

                    opsi = input("Beli buah yang lain (y/n) ? ")
                    if(opsi=='y') :
                        lanjut = True
                    
                    elif(opsi=='n') :
                        lanjut = False

                    else :
                        print('Inputan Invalid')
                        break
                      
            else :
                print("Maaf, buah yang anda masukkan tidak ada")

        print("-------------------------------------------")
        print("Total Harga : ", sum(total))

    except ValueError :
        print("Silahkan jumlah buah dengan benar")
        jumlahBuah()


