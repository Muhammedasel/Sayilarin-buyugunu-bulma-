a= input("ilk sayıyı giriniz : ")

b= input("ikinci sayıyı giriniz : ")

c= input("üçüncü sayıyı giriniz : ")

if(a>b and a>c ):
    print(" {} {} ve {} 'den büyüktür. ".format(a,b,c))

elif(b>a and b>c ):
    print("{} {} ve {} 'den büyüktür. ".format(b,a,c))

elif(c>a and c>b ):
    print("{} {} ve {} den büyüktür. ".format(c,a,b))

else:
    print("HATALI GİRİŞ YAPTINIZ..")
