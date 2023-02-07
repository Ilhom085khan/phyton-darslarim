# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:31:34 2023

@author: VICTUS
"""

#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.

#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#    if car=="gm":
#        print(car.upper())
#    else:
#        print(car.title())


#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.

#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#    if car!="gm":
#        print(car.title())
#    else:
#        print(car.upper())


#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.

#ism=input("login ismingizni kiriting\n>>>")
#if ism.lower()=="admin":
#    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
#else:
#    print(f"Xush kelibsiz, {ism.title()}!")

#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.

#print("2ta son kiriting")
#a=float(input("1-sonni kiriting\n>>>"))
#b=float(input("2-sonni kiriting\n>>>"))
#if a==b:
#    print("Busonlar bir biriga teng!!!")


#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.

#x=float(input("Istalgan son kiriting\n>>>"))
#if x>0:
#    print("Bu son musbat son")
#elif x==0:
#    print("Bu son neytral son")    
#else:
#    print('bu son manfiy son')
    
    
#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.

#x=float(input('Istalgan turdagi sonni kiriting\n>>>'))
#if x>=0:
#    print(x**(1/2))
#else:
#    print("Musbat son kiriting")