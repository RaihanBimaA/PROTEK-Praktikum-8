dataNama=[]
i=True
while(i==True):
    nama=input('Masukkan nama:')
    dataNama.append(nama)
    Lanjut=input('Input nama lagi?(y/n)')
    if(Lanjut=='y'):
        i=True
    elif(Lanjut=='n'):
        i=False
    else:
        print('Inputan Invalid')
        break
print()
dataNama.sort()
for x in range(len(dataNama)):
    print(dataNama[x],'(',len(dataNama[x]),'karakter)')
    
