import random

def Topla(*sayilar): #Sınırsız Argüman girilebilir *
    sonuc = 0
    for sayi in sayilar:
        sonuc += sayi
    return sonuc

def Cikar(sayi1,sayi2):
    return sayi1 - sayi2

numbers = [4, 8, 15, 16, 23, 42]
print(Topla(*numbers)) #numbers listesini tamamen ayrı ayrı argüman olarak yazar *
print(Cikar(12, 4))

'''
Birden Fazla Satır Comment
Nice
'''

for sayi in range(1, 10): #For Döngüsü 1 den 10a  kadar 10 dahil değil
    print(sayi)

bag = [1, 2, 3, 4, 5]
'''
for i in range(len(bag)):
    bag[i]= bag[i]* 2
'''
bag = [elem * 2 for elem in bag] #Yukarıdaki ile aynı işlemi tek satırda. Her bir elementi tek tek işler
print(bag)

names = ["John", "Ridley", "Burak"]
print("İsimler :", ', '.join(names)) #İsimleri ',' karakteri ile ayırarak string yapıyor

print(random.randrange(1, 100))
