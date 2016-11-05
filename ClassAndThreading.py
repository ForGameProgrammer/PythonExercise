import threading

class Heyyo():
    age = 21
    def __init__(self, name): # __init__ class oluşturulunca çağırılır self olmazsa olmaz
        self.name = name
        print(self.name)
        print(self.age) # direk age diyemiyoruz self olması gerekiyor kendi class ının alması için


class GoodName(threading.Thread): # GoodName class inheritance from Thread Class
    def run(self):
        for _ in range(10): # Değişkeni kullanmayacaksak sadece döngü içinse _ adını verebiliriz
            print(threading.currentThread().getName())

th1 = GoodName(name="Thread 1") # name değişkeni Thread class'ından geliyor
th2 = GoodName(name="Thread 2")

th1.start()
th2.start()