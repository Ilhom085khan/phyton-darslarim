# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:33:12 2023

@author: VICTUS
"""

#Yoydalanuvchidan juft son kiritishni sorang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

#son=int(input("Juft son kiriting!\n>>>"))
#juft=range(0,50,2)
#toq=range(1,50,2)
#if son in juft:
#    print("Rahmat!!!")
#elif son in toq:
#    print("Bu son juft emas!!!")

#Foydalanuvchi yoshini sorang, va muzeyga kirish uchun chipta narxini quyidagicha kiriting:
    #Agar foydalanuvchi 4 yoshdan kichkina bolsa yoki 60 dankatta bolsa bepul
    #Agar foydalanuvchi 18dan kichik bolsa 10000 som
    #Agar foydalanuvchi 18dan katta bolsa 20000 som
#narx=0
#yosh=int(input("Yoshingiz nechida?>>>"))
#if yosh<=4 or yosh>=60:
#    narx=narx+0
#elif yosh<=18:
#    narx=narx+1000
#else:
#    narx=narx+2000
#print(f"Sizga chipta narxi {narx} som")


#Foydalanuvchidan ikkita son kiritishini sorang, sonlarni solishtiring va ularning teng yoki katta kichikligi haqida xabarni chiqaring.

#a=int(input("Birinchi sonni kiriting\n>>>"))
#b=int(input("Illinchi sonni kiriting\n>>>"))
#if a>b:
#    print(f"{a}>{b}")
#elif a<b:
#    print(f"{a}<{b}")
#else:
#    print(f"{a}={b}")
    
    
#mahsulotlar degan royxat yarating va kamida 10ta turli mahsulotni kiriting. Yangi, savat degan bosh royxat yarating va foydalanuvchidan savatga kamida 5ta mahsulot kiritishni sorang. Savatdagi elementlarni, mahsulotlar royxati bn solishtiring va qaysi biri royxatda bolsa "Mahsulot dokonimizda bor" aks holda, "Mahsulot do'konimizda yoq" degan xabarni chiqaring.

#mahsulotlar=["kartoshka","piyoz","sabzi","karam","cola","pepsi","tuxum","qalam","ruchka","shakar"]
#savat=[]
#for savol in range(5):                                                                                                      
#    savol=(input("Olmoqchi bo'lgan mahsulotlaringizni kiriting\n>>>"))
#    savat.append(savol)
#for n in savat:
#    if n in mahsulotlar:
#        print(f"{n} bizning do'konimizda bor")
#    else:
#        print(f"Bizning do'konimizda {n} yoq")
        
        
#Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yangi, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

#mahsulotlar=["kartoshka","piyoz","sabzi","karam","cola","pepsi","tuxum","qalam","ruchka","shakar"]
#savat=[]
#for i in range(5):
#    savat.append(input(f"Olmoqchi bo'lgan {i+1}- mahsulotingizni kiriting\n>>>"))
#bor_mahsulotlar=[]
#yoq_mahsulotlar=[]
#for n in savat:
#    if n in mahsulotlar:
#        bor_mahsulotlar.append(n)
#    else:
#        yoq_mahsulotlar.append(n)
#if len(yoq_mahsulotlar)==0:
#    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
#else:
#    print(f"Quyidagi mahsulotlar do'konimizda yo'q:{yoq_mahsulotlar}")


#foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

#login=["ilhomomonqulov1@gail.com","azizazimov34@gamail.com","abbosjabborov@gmail.com","ruslanchinnibekov@gmail.com"]
#ism=input("O'zingizga login tanlang\n>>>")
#if ism in login:
#    print("Urz bu login band")
#else:
#    print("Xush kelibsiz")

#Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
    
#son = int(input("Istalgan butun son kiriting: "))
#for n in range(2,11):
#    if not (son%n):
#        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")