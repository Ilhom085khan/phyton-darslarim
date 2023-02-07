# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:30:23 2023

@author: VICTUS
"""

#O'zingizga malum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
#Ro'yxatning uzunligini konsolga chiqaring
#sorted() funksiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
#Asl ro'yxatni qaytadan konsolga chiqaring
#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring

#davlatlar=["saudiya arabistoni","xitoy","amerika","norvegiya","rassiya","angliya","fransiya","germaniya"]
#print(davlatlar)
#print(len(davlatlar))
#print(sorted(davlatlar))
#print(sorted(davlatlar,reverse=True))
#print(davlatlar)
#print(davlatlar.reverse())
#print(davlatlar)
#print(davlatlar.sort())
#print(davlatlar)
#print(davlatlar.sort(reverse=True))
#print(davlatlar)


#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
#Ro'yxatdagi sonlar yigindisini hisoblang va konsolga chiqaring
#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisiblang va konsolga chiqaring
#Ro'yxatdagi elementlar sonini hisoblang
#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring

#sonlar=list(range(120,1201,2))
#print(sum(sonlar))
#print(max(sonlar)-min(sonlar))
#print(len(sonlar))
#print(sonlar[0:21],sonlar[260:281],sonlar[520:541])


#taomlar degan ro'yxat yarating va ichiga istalgan 5 ta taomni kiriting
#nonushta degan yangi ro'yxatga taomlardan nusxa oling
#Yangi ro'yxatni faqat nonushtaga yeyiladigan taomlarni qoldiring, va qoshimcha 2ta taom qo'shing
#ikkala ro'yxatni ham (taomlar va nonushta) konsulga chiqaring
#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0]="qaymoq va non" deb qiymat berib ko'ring

#taomlar=["osh","manti","somsa","shashlik","qovirma"]
#nonushta=taomlar[:]
#print(nonushta.remove("osh"))
#print(nonushta.remove("qovirma"))
#print(nonushta.append("salat"))
#print(nonushta.append("pirok"))
#print(f"{taomlar}\n{nonushta}")
#nonushta=tuple(nonushta)
#nonushta[0]="qaymoq va non"