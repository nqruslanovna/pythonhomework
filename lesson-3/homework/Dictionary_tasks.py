# 1 Qiymatni olish: Agar lug'at va kalit berilgan bo'lsa, agar kalit mavjud bo'lmasa,
#  nimani qaytarish kerakligini hisobga olib, tegishli qiymatni oling.
# person = {
#            'name': 'Humayro'
# }
# person1 = {}
# print(bool(person1))
# print(bool(person))

# 2 Kalitni tekshirish: Lug'at va kalit berilgan bo'lsa, kalit lug'atda mavjudligini tekshiring.
# person = {'name': 'Humayro'}
# if bool(person.keys())==True:
#     print('kalit mavjud')

# 3 Hisoblash tugmalari: Lug'atdagi kalitlar sonini aniqlang.
# dic = {
#     'qizil': '100',
#     'sariq': '40',
#     'yashil': '1000',
# }
# print(len(dic.keys()))

# 4 Barcha kalitlarni oling: Lug'atdagi barcha kalitlarni o'z ichiga olgan ro'yxat yarating.
# dic = {
#     'qizil': '100',
#     'sariq': '40',
#     'yashil': '1000',
# }
# print(dic.keys())

# 5 Barcha qiymatlarni oling: Lug'atdagi barcha qiymatlarni o'z ichiga olgan ro'yxat yarating.
# dic = {
#     'qizil': '100',
#     'sariq': '40',
#     'yashil': '1000',
# }
# print(dic.values())


# 6 Lug'atlarni birlashtirish: Ikkita lug'at berilgan bo'lsa, ikkalasini birlashtirgan yangi lug'at yarating.
# dic1 = {"maqsad": '200', 'intilish': '300', 'harakat': "900"}
# dic2 = {'qiyinchilik':'1200', 'natija': '9999'}
# a = list(dic1.items())
# b = list(dic2.items())
# a.extend(b)
# print(dict(a))

# 7 Kalitni olib tashlash: Agar lug'at va kalit berilgan bo'lsa,
#  agar mavjud bo'lsa, kalitni olib tashlang, agar mavjud bo'lmasa, ishni boshqaring.
# dic = {'ismim': 'Nozimaxon'}
# if bool(dic.keys())==False:
#     print('key mavjud emas')
# elif bool(dic.keys())==True:
#     print('key mavjud va quyidagicha:', dic.keys())

# 8 Lug'atni tozalash: Yangi bo'sh lug'at yarating.
# dic = {'1':'bir','2':'ikki'}
# diclist = list(dic.items())
# diclist.pop()
# diclist.pop()
# print(dict(diclist))

# 9 Lug'at bo'sh yoki yo'qligini tekshiring: Lug'atda biron bir element mavjudligini aniqlang.
# dic = {}
# if bool(dic)==False:
#     print("dictionary bo'sh")
# elif bool(dic)==True:
#     print("dictionary bo'shmas")


# 10 Kalit-qiymat juftligini oling:
#  Agar lug'at va kalit berilgan bo'lsa, kalit mavjud bo'lsa, kalit-qiymat juftligini oling.
# dic = dict(bir='1',ikki='2',uch='3')
# dic.items()
# print(dic)



# 11 Yangilash qiymati: Lug'at berilganda, belgilangan kalit uchun qiymatni yangilang.
# dic = dict(yosh='3',ism='Soliha')
# dic.update(yosh='4')
# print(dic)




# 12 Qiymatli hodisalarni hisoblash:
#  Lug'at berilganda, ma'lum bir qiymat kalitlar bo'ylab necha marta paydo bo'lishini hisoblang.
# dic = dict(yosh='2',ism='Ali',yil='2')
# a = list(dic.values())
# print(a.count('2'))




# 13 Lug'atni o'zgartir: Lug'at berilgan bo'lsa, kalit va qiymatlarni almashtiradigan yangi lug'at yarating.
# dic = dict(yosh='3',ism='Soliha')
# diclist = list(dic.items())
# diclist.pop()
# diclist.pop()
# dic1 = dict(diclist)
# print(dic1)
# dic1.update(meva='olma',gul='lola')
# print(dic1)



# 14 Qiymatli kalitlarni toping:
#  Lug'at va qiymatni hisobga olgan holda, ushbu qiymatga ega bo'lgan barcha kalitlar ro'yxatini yarating.
# dic = {"maqsad": '200', 'intilish': '300', 'harakat': "900"}
# keylist = list(dic.keys())
# print(keylist)


# 15 Roʻyxatlardan lugʻat yarating:
#  ikkita roʻyxatni (bir kalit va bitta qiymat) hisobga olib, ularni juftlashtiruvchi lugʻat yarating.
# my_list1 = ['ism','familiya']
# my_list2 = ['Nozimaxon','Quvondiqova']
# new_list = [[my_list1[0],my_list2[0]],[my_list1[1],my_list2[1]]]
# print(dict(new_list))





# 16 Ichki lug'atlarni tekshiring: Lug'at berilgan bo'lsa, qiymatlar ham lug'at ekanligini tekshiring.
# 17 Ichki qiymatni oling: Ichki lug'at berilgan bo'lsa, ichki lug'atlardan biridagi qiymatni oling.


# 18 Standart lug'at yaratish: etishmayotgan kalitlar uchun standart qiymatni ta'minlaydigan lug'at yarating.
# dic = dict(bir='1',ikki='2')
# dic.update(uch='3',four='4')
# print(dic)


# 19 Noyob qiymatlarni sanash: Lug'at berilgan bo'lsa, undagi noyob qiymatlar sonini aniqlang.
# dic = {"maqsad": '200', 'intilish': '300', 'harakat': "900"}
# print(len(list(dic.values())))

# 20 Lug'atni kalit bo'yicha saralash: Tugmalar bo'yicha tartiblangan yangi lug'at yarating.
# dic = dict(ism='soliha',familiya='quvondioqva',ochestva='navrozbekovna',yosh='3')
# k = list(dic.keys())
# l1 = k[0:2]
# l2 = k[2:4]
# new_list = [[l1[0],l2[0]],[l1[1],l2[1]]]
# print(dict(new_list))



# 21 Lug'atni qiymat bo'yicha saralash: qiymatlar bo'yicha saralangan yangi lug'at yarating.
# dic = dict(ism='soliha',familiya='quvondioqva',ochestva='navrozbekovna',yosh='3')
# k = list(dic.values())
# l1 = k[0:2]
# l2 = k[2:4]
# new_list = [[l1[0],l2[0]],[l1[1],l2[1]]]
# print(dict(new_list))

# 22 Qiymat boʻyicha filtrlash: Lugʻat berilgan boʻlsa, 
# faqat maʼlum shartlarga javob beradigan qiymatlarga ega elementlarni oʻz ichiga olgan yangi lugʻat yarating.

# 23 Umumiy kalitlarni tekshiring:
#  ikkita lug'at berilgan bo'lsa, ularning umumiy kalitlari bor yoki yo'qligini tekshiring.
# dic1 = dict(bir='1',ikki='2',uch='3')
# dic2 = dict(bir='4',ikki='5')
# s1 = set(dic1.keys())
# s2 = set(dic2.keys())
# if s1&s2==set():
#     print('umumiy key yoq')
# elif s1&s2!=set():
#     print('umumiy key mavjud')



# 24 Tuple'dan lug'at yaratish: kalit-qiymat juftliklari to'plamini hisobga olib, undan lug'at yarating.
# t1 = (1,2,3,4)
# t2 = ('one','two','thee','four')
# l1 = list(t2)
# l2 = list(t1)
# dic =dict(zip(l1,l2))
# print(dic)



# 25 Birinchi kalit-qiymat juftligini oling: birinchi kalit-qiymat juftligini lug'atdan oling.
# dic = dict(ism='Nozimaxon',familiya='Quvondiqova')
# diclist = list(dic.items())
# print(diclist[0])


