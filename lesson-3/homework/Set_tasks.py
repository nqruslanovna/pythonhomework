#1 Union of Sets: Given two sets, create a new set that contains all unique elements from both sets.
# s1 = {1,2,3,99}
# s2 = {4,5,6,100}
# s1list = sorted(s1)
# s2list = sorted(s2)
# print(set([s1list[3],s2list[3]]))

# 2 Intersection of Sets: Given two sets, create a new set that contains elements common to both sets.
# To'plamlarning kesishishi: Ikki to'plam berilgan bo'lsa, 
# ikkala to'plam uchun umumiy elementlarni o'z ichiga olgan yangi to'plam yarating.
# s1 = {1,2,3,4}
# s2 = {3,4,5,6,7}
# print(s1 & s2)

# 3 To'plamlarning farqi: Ikki to'plam berilgan bo'lsa, 
# birinchi to'plamning ikkinchisida bo'lmagan elementlari bilan yangi to'plam yarating.
# s1 = {'a','b','c','d','e','f'}
# s2 = {'m','n','p','q','c','d'}
# print(s1-s2)

# 4 Pastki toʻplamni tekshiring: 
# Ikki toʻplam berilgan boʻlsa, bir toʻplam boshqasining quyi toʻplami ekanligini tekshiring.
# s1 = {1,2,3,4,5,6}
# s2 = {3,4}
# s3 = {7,8}
# print(s2<=s1)
# print(s3<=s1)

# 5 Elementni tekshiring: To'plam va element berilgan bo'lsa, to'plamda element mavjudligini tekshiring.
# s = {'a','b','c','d'}
# s1 = {'c'}
# s2 = {'f'}
# print(s>=s1)
# print(s>=s2) 

# 6 To'plam uzunligi: to'plamdagi noyob elementlar sonini aniqlang.
# s = {1,2,3,4,5,6,7,8,7,7,7,6,6,5,5,3,3,2,2,1,1}
# print(len(s))

# 7 Roʻyxatni toʻplamga aylantirish: Roʻyxat berilgan boʻlsa,
#  ushbu roʻyxatdagi faqat noyob elementlarni oʻz ichiga olgan yangi toʻplam yarating.
# s = {0,1,2,3,4,5,6,7,8,9}
# slist  = list(s)
# print(set(slist[4:7]))

# 8 Elementni olib tashlash: To'plam va element berilgan bo'lsa, agar mavjud bo'lsa, elementni olib tashlang.
# s = {0,1,2,3,4,5,6,7,8,9}
# slist = list(s)
# slist.remove(7)
# print(set(slist))

# 9 To‘plamni tozalash: Mavjud to‘plamdan yangi bo‘sh to‘plam yarating.
# s = {1,2,3,4,5}
# s.clear()  
# print(s)

# 10 To'plam bo'sh yoki yo'qligini tekshiring: to'plamda biron bir element mavjudligini aniqlang.
# s1 = {}
# s2 = {1,2}
# print(bool(s1))
# print(bool(s2))

# 11 Simmetrik farq: ikkita to'plam berilgan bo'lsa, ikkala to'plamda bo'lmagan,
#  ammo ikkalasida ham bo'lmagan elementlarni o'z ichiga olgan yangi to'plam yarating.
# s1 = {'a','b','c','d','e','f'}
# s2 = {'m','n','p','q','c','d'}
# print(s1^s2)

# 12 Element qo'shish: To'plam va elementni hisobga olgan holda, element mavjud bo'lmasa, to'plamga qo'shing.
# s = {1,2,3,4,5,6,7,8,9}
# slist = list(s)
# slist.append(20)
# print(set(slist))

# 13 Pop Element: Toʻplam berilgan boʻlsa, toʻplamdan ixtiyoriy elementni olib tashlang va qaytaring.
# s = {1,2,3,4,5,6,7,8,9}
# slist = list(s)
# slist.remove(slist[4])
# print(set(sorted(slist)))

# 14 Maksimalni toping: Berilgan raqamlar to'plamidan maksimal elementni toping.
# s = {0,1,2,3,4,5,6,7,8,9}
# print(max(s))

# 15 Minimalni toping: berilgan sonlar to‘plamidan minimal elementni toping.
# s = {0,1,2,3,4,5,6,7,8,9}
# print(min(s))

# 16 Juft sonlarni filtrlash: Butun sonlar to‘plamini hisobga olgan holda,
#  faqat juft sonlarni o‘z ichiga olgan yangi to‘plam yarating.
# s = {1,2,3,4,5,6,7,8}
# slist = list(s)
# snew = set([slist[1],slist[3],slist[5],slist[7]])
# print(snew)


# 17 Toq raqamlarni filtrlash: 
# Butun sonlar to‘plamini hisobga olgan holda, faqat toq raqamlardan iborat yangi to‘plam yarating.
# s = {1,2,3,4,5,6,7,8}
# slist = list(s)
# snew = set([slist[0],slist[2],slist[4],slist[6]])
# print(snew)


# 18 Diapazon to‘plamini yarating:
#  Belgilangan diapazonda raqamlar to‘plamini yarating (masalan, 1 dan 10 gacha).
# print(set(range(72,88)))

# 19 Birlashtirish va takroriy nusxalash: Ikkita roʻyxatni hisobga olgan holda, 
# ikkala roʻyxatni birlashtirgan va dublikatlarni olib tashlaydigan yangi toʻplam yarating.
# s1 = {1,2,3,4,5,14,15}
# s2 = {1,2,11,12,13,14,15}
# print(s1|s2)

# 20 Ajratilgan to'plamlarni tekshiring: 
# ikkita to'plam berilgan bo'lsa, ularda umumiy elementlar yo'qligini tekshiring.
# s1 = {1,2,3,4,5}
# s2 = {6,7,8,9}
# if s1 & s2 == set():
#     print('bosh toplam')
# else:
#     print('umumiy element mavjud')

# 21 Roʻyxatdagi dublikatlarni olib tashlash: Roʻyxat berilgan boʻlsa,
#  undan dublikatlarni olib tashlash uchun toʻplam yarating, soʻngra yana roʻyxatga aylantiring.


# 22 Noyob elementlarni sanash: Ro'yxat berilgan, to'plamdan foydalanib noyob elementlar sonini aniqlang.
# s = {1,3,4,5,6,7,8,9,0,5,4,3,2,5,6,7,8}
# print(len(s))



# 23 Tasodifiy to'plam yaratish:
#  ma'lum bir diapazonda belgilangan tasodifiy butun sonlar bilan to'plam yarating.
# print(set(range((-3),10)))
