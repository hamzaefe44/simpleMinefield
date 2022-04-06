import random


m=[[' ' for i in range(10)] for j in range(10)]#10x10 luk mayınsız bir matris oluşturduk

m_line=[]
m_culumn=[]

for i in range(30):#mayın tarlamıza eklenecek mayınların konumlarını random atama işlemi gerçekleştiriyoruz
    m_line.append(random.randint(1,9))
    m_culumn.append(random.randint(1,9))

mine=[(i,j) for (i,j) in zip(m_line,m_culumn)]#30 adet mayinimizin, mayın tarlasındaki konumlarını tupleler halinde listede depoluyoruz

for i in mine:
    line=i[0]
    culumn=i[1]

    m[line][culumn]='x'#10x10'luk mayın tarlamıza mayın ekleme işlemi

for line in m:#mayin tarlamızın çıktısı
    print(line)


x=True
while(x):#kullanicidan satır ve sutun alarak mayınlara basıp basmadığını kontrol ediyoruz
    print("""0 ile 9 arasında değer giriniz""")

    line_index=int(input("satir index:"))
    culumn_index=int(input("sutun index:"))

    if m[line_index][culumn_index]=="x":
        print("You stepped on a mine!!!")
        break
    else:
        print("You won!!!")
