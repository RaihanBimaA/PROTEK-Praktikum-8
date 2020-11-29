def dataStat(x):
    dataTuple=tuple(x)
    a=sum(x)/len(x)
    b=max(dataTuple)
    c=min(dataTuple)
    datanya=[a,b,c]
    return datanya
while True:
    try:
        n=int(input('Berapa banyak angka yang ingin diinput?:(harus angka):'))
        break
    except ValueError:
        print('Input Invalid')
        continue
data=[]
i=1
while(i<=n):
    try:
        bilangan=int(input('Masukan angka anda:'))
        data.append(bilangan)
        i+=1
    except ValueError:
        print('Input Invalid')
hasilData=dataStat(data)
print(hasilData)
