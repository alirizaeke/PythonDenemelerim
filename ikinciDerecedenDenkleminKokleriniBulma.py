import time
from math import sqrt

print("ax^2 + bx + c = 0 formatındaki ikinci dereceden denklemin kökleri hesaplanacaktır")
print("Eğer ondalıklı sayı girecekseniz lütfen virgül değil nokta kullanınız")
a = float(input("Lütfen a değerini giriniz: "))
b = float(input("Lütfen b değerini giriniz: "))
c = float(input("Lütfen c değerini giriniz: "))

delta = b**2-4*a*c

if delta == 0 :
    x1 = (-b+sqrt(delta))/(2*a)
    print("Çift katlı kök:",x1)
elif delta > 0 :
    x1 = (-b+sqrt(delta))/(2*a) #son parantezin önemini saatlerimi kaybederek öğrenmiştim
    x2 = (-b-sqrt(delta))/(2*a) #çok sinir bozucu bir durum
    
    print("Birinci kök: ",x1)
    print("İkinci kök: ",x2)
else:
    x1 = (-b+sqrt(-delta))/(2*a)
    x2 = (-b-sqrt(-delta))/(2*a)
    
    print("Birinci sanal kök: ",x1,"i")
    print("İkinci sanal kök: ",x2,"i")
    
time.sleep(10)

