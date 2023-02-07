# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:29:53 2023

@author: VICTUS
"""

#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:

#ismlar=['ilhom','ozim','omonqulov ilhom','omonqulov ilhom nasriddinovich']
#for dost in ismlar:
#    print("sen mening eng iwongan insonimsan",dost)


#sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
#yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.

#sonlar=[32,-34,0.7,67.34]
#print((sonlar[0]+8)*1/2)
#print(sonlar[1]+34)
#print(f"{sonlar[1]+sonlar[0]}")
#print(sonlar[0]+sonlar[1])
#sonlar[2]=0
#print(sonlar)


#t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:

#t_shaxslar=["amir temur","alisher navoiy","nyuton","enshtein","mirzo ulug'bek"]    
#z_shaxslar=["subyektiv","timur alixanov","konsta","ilon mask","dadam"]
#print(f"Men tarixiy shaxslardan {(t_shaxslar.pop(3)).title()}bilan va zamonaviy shaxslardan {(z_shaxslar.pop(4)).title()} bilan suhbatlashishni hohlayman")


#friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing

#friends=[]
#mehmonlar=[]
#friends.append("norov aziz")
#friends.append('abbos')
#friends.append('xushnut')
#friends.append('abdulla')
#friends.append('diyor')
#friends.remove('abdulla')
#friends.remove('diyor')
#friends.insert(0,'abdulla')
#friends.insert(-1,'diyor')
#friends.insert(2,'otamurod')
#print(mehmonlar.append(friends.pop(0)))
#print(mehmonlar.append(friends.pop(0)))
#print(mehmonlar.append(friends.pop(0)))
#print(mehmonlar.append(friends.pop(0)))
#print(f"Mehmonga {mehmonlar}lar keldi,\n{friends}lar kelmadi")