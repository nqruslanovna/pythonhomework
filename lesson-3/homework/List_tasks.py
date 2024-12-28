#1 Hodisalar soni: Roʻyxat va element berilgan boʻlsa, element roʻyxatda necha marta paydo boʻlishini toping.
# a = ['a','b','d','a','a','l','a']
# print(a.count('a'))

#2 Elementlar yig'indisi: raqamlar ro'yxati berilgan, barcha elementlarning umumiy miqdorini hisoblang.
# royxat = ['1','2','3','4','5','6']
# print(len(royxat))

# print(int(royxat[0])+int(royxat[1])+int(royxat[2])+int(royxat[3])+int(royxat[4])+int(royxat[5]))

#3 Maksimal element: Berilgan ro'yxatdan eng katta elementni aniqlang.
# my_list = ['1','2','3','4','5','6']
# print(max(my_list)) 

#4 Min element: Berilgan roʻyxatdan eng kichik elementni aniqlang.
# my_list = ['1','2','3','4','5','6']
# print(min(my_list)) 

#5 Elementni tekshiring: Ro'yxat va element berilgan bo'lsa, element ro'yxatda mavjudligini tekshiring.
# my_list = ['apple','banana','strawberry', 'cherry','melon']
# if my_list.count('melon'):
#     print('listda melon mavjud')


#6 Birinchi element: Roʻyxat boʻsh boʻlsa, nimani qaytarish kerakligini hisobga olib, 
# roʻyxatning birinchi elementiga kiring.
# my_list = [1,2]
# if bool(my_list)==False:
#     print('list bosh')
# elif bool(my_list)==True:
#     print('listning birinchi elementi:',my_list[0])



#7 Oxirgi element: Roʻyxat boʻsh boʻlsa, nimani qaytarish kerakligini hisobga olib, 
# roʻyxatning oxirgi elementiga kiring.
# my_list = [1,2]
# if bool(my_list)==False:
#     print('list bosh')
# elif bool(my_list)==True:
#     print('listning oxirgi elementi:',my_list[-1])


#8 Bo'limlar ro'yxati: Asl ro'yxatning faqat birinchi uchta elementini o'z ichiga olgan yangi ro'yxat yarating.
# my_list = ['1','2','3','4','5','6']
# print(my_list[0:3])

#9 Teskari ro'yxat: Asl ro'yxat elementlarini teskari tartibda o'z ichiga olgan yangi ro'yxat yarating.
# my_list = ['1','2','3','4','5','6']
# my_list.reverse()
# print(my_list)

#10 Saralash roʻyxati: Asl roʻyxat elementlarini tartiblangan tartibda oʻz ichiga olgan yangi roʻyxat yarating.
# my_list = ['3', '4', '6', '1', '2', '5']
# print(sorted(my_list))

#11 Dublikatlarni o'chirish: Ro'yxatni hisobga olgan holda, 
# asl ro'yxatdagi faqat noyob elementlarni o'z ichiga olgan yangi ro'yxat yarating.
# my_list = ['1','a','3','b','6','4','c']
# my_list.remove(my_list[0])
# my_list.remove(my_list[1])
# my_list.remove(my_list[2])
# my_list.remove(my_list[2])
# print(my_list)


#12 Elementni qo'shish: Ro'yxat va elementni hisobga olgan holda, elementni belgilangan indeksga kiriting.
# my_list = ['aa','bb','cc']
# my_list1 = my_list[:]
# my_list1.insert(1,"aaa")
# print(my_list1)

#13 Element indeksi: Roʻyxat va element berilgan boʻlsa, elementning birinchi paydo boʻlish indeksini toping.
# my_list = ['b','a','d','a','a','l','a']
# print(my_list.index("a"))

#14 Bo'sh ro'yxatni tekshiring: ro'yxat bo'sh yoki yo'qligini aniqlang va mantiqiy qiymatni qaytaring.
# my_list = []
# print(bool(my_list))

#15 Juft sonlarni sanash: Butun sonlar ro‘yxati berilgan bo‘lsa, ularning nechtasi juft ekanligini hisoblang.
# my_list = [1,2,3,4,5,6,7,8]
# print('listdagi juft sonlar soni:',len(my_list)//2)

#16 Toq sonlarni sanash: Butun sonlar roʻyxati berilgan boʻlsa, ularning qanchasi toq ekanligini hisoblang.
# my_list = [1,2,3,4,5,6,7,8,]
# if len(my_list)%2==0:
#     toq = len(my_list)//2
# elif len(my_list)%2!=0:
#     toq = len(my_list)//2+1
# print('listdagi toq sonlar soni:' ,toq)

# #17 Roʻyxatlarni birlashtirish: Ikki roʻyxatni hisobga olgan holda, ikkala roʻyxatni birlashtirgan yangi roʻyxat yarating.
# my_list1 = ['1','2','3']
# my_list2 = ['a','b','c']
# my_list1.extend(my_list2)
# print(my_list1)

#18 Qo'shimcha ro'yxatni toping: 
# Ro'yxat va pastki ro'yxatni hisobga olgan holda, ro'yxatda quyi ro'yxat mavjudligini tekshiring.
# my_list = [1,2,3,4,[5,6],7,8,9,9,9,9]
# my_l = my_list[4]
# if bool(my_l)==True:
#     print('sublist mavjud')




#19 Elementni almashtirish: Roʻyxat berilgan boʻlsa, koʻrsatilgan elementning birinchi paydo boʻlishini boshqa element bilan almashtiring.
# my_list = ['b','a','d','a','a','l','a']
# a = my_list.index('a')
# my_list1 = my_list[:]
# my_list1.insert(a,8)
# print(my_list1)

#20 Ikkinchi eng katta elementni toping: Berilgan ro'yxatdan ikkinchi eng katta elementni toping.
# my_list = ['3', '4', '6', '1', '2', '5']
# my_list1 = my_list.remove(max(my_list))
# print(max(my_list))

#21 Ikkinchi eng kichik elementni toping: Berilgan ro'yxatdan ikkinchi eng kichik elementni toping.
# my_list = ['3', '4', '6', '1', '2', '5']
# my_list1 = my_list.remove(min(my_list))
# print(min(my_list))


#22 Roʻyxat uzunligi: Roʻyxatdagi elementlar sonini aniqlang.
# my_list = ['3', '4', '6', '1', '2', '5']
# print(len(my_list))

#23 Nusxa yaratish: Asl roʻyxatning nusxasi boʻlgan yangi roʻyxat yarating.
# my_list = ['a','b','c']
# my_list1 = my_list.copy()
# print(my_list)
# print(my_list1)

#24 O'rta elementni oling: ro'yxat berilgan, o'rta elementni toping. 
# Agar ro'yxatda juft sonli elementlar bo'lsa, ikkita o'rta elementni qaytaring
# my_list = ['3', '4', '6', '1', '2', '5']
# x = (len(my_list))
# print(my_list[int(x/2-1)])
# print(my_list[int(x/2)])

# my_l = [ '4', '6', '1', '2', '5']
# y = (len(my_l))
# print(my_l[int(x/2-1)])

#25 Qo'shimcha ro'yxatning maksimal qismini toping:
#  Ro'yxat berilgan bo'lsa, belgilangan pastki ro'yxatning maksimal elementini toping.
# my_list = [1, 2, [3,4,5,6,7],8,9]
# my_l = my_list[2]
# print(max(my_l))

#26 Find Minimum of Sublist: Given a list, find the minimum element of a specified sublist.
# my_list = [1, 2, [3,4,5,6,7],8,9]
# my_l = my_list[2]
# print(min(my_l))

#27 Remove Element by Index: Given a list and an index, remove the element at that index if it exists.
# Elementni indeks bo'yicha olib tashlash: Ro'yxat va indeks berilgan bo'lsa, 
# agar mavjud bo'lsa, ushbu indeksdagi elementni olib tashlang.
# my_list = [1, 2, [3,4,5,6,7],8,9]
# my_list.remove(my_list[2])
# print(my_list)

#28 Ro'yxat tartiblanganligini tekshiring: 
# Ro'yxat o'sish tartibida tartiblanganligini aniqlang va mantiqiy qiymatni qaytaring.
# Check if List is Sorted: Determine if the list is sorted in ascending order and return a boolean.
# my_list = ['3', '4', '6', '1', '2', '5']
# my_list1 = ['1','2','3','4','5','6']
# my_list2 = sorted(my_list)
# my_list3 = sorted(my_list1)
# print(bool(my_list2==my_list))
# print(bool(my_list3==my_list1))

#29 Elementlarni takrorlash: Roʻyxat va raqam berilgan boʻlsa, 
# har bir element bir necha marta takrorlanadigan yangi roʻyxat yarating.
# my_list = ['olma','olcha','banan','anor','gilos','dovcha','gilos','qulupnay','rujja']
# my_list.append(my_list[0])
# my_list.append(my_list[2])
# my_list.append(my_list[5])
# my_list.append(my_list[8])
# my_list.append(my_list[3])
# print(my_list)

#30 Birlashtirish va saralash: 
# Ikki roʻyxatni hisobga olgan holda, ikkala roʻyxatni birlashtirgan yangi tartiblangan roʻyxat yarating.
# my_list1 = [1,34,56,996,754]
# my_list2 = [5,95,1002,2005]
# my_list1.extend(my_list2)
# sorted(my_list1)
# print(my_list1)

#31 Barcha indekslarni toping:
#  Ro'yxat va element berilgan bo'lsa, ro'yxatdagi ushbu elementning barcha indekslarini toping.
# my_list = ['b','a','d','a','a','l','a']
# a = int((my_list.index('a')))
# b = int(my_list.index('a', a+1))
# c = int(my_list.index('a',b+1))
# d = int(my_list.index('a',c+1))
# print("listda ", a,',',b,',',c,',',d, 'indexlarda "a" elementi joylashgan')

#32 Ro'yxatni aylantirish: Ro'yxat berilgan bo'lsa,
#  asl ro'yxatning aylantirilgan versiyasi bo'lgan yangi ro'yxat yarating (elementlarni o'ngga siljitish).



#33 Ranglar roʻyxatini yaratish: 
# Belgilangan diapazondagi raqamlar roʻyxatini yarating (masalan, 1 dan 10 gacha).
# print(list(range(10,20)))

#34  musbat raqamlar yig'indisi:
#  raqamlar ro'yxati berilgan, barcha musbat raqamlarning yig'indisini hisoblang.
# my_list = [1,2,-3,4,-5]
# summ = my_list[0] + my_list[1]+my_list[3]
# print(summ)
    

#35 manfiy raqamlar yig'indisi: raqamlar ro'yxati berilgan,
#  barcha manfiy sonlarning yig'indisini hisoblang.
# my_list = [1,2,-3,4,-5]
# summ = my_list[2] + my_list[4]
# print(summ)


#36 Palindromni tekshiring: Roʻyxat berilgan boʻlsa,
#  roʻyxat palindrom yoki yoʻqligini tekshiring (oldinga va orqaga bir xil oʻqiydi).
# my_list = [1,2,3,2,1]
# my_list1 = [1,2,3,4,5]
# my_list.reverse()
# my_list1.reverse()
# print(my_list == [1,2,3,2,1] )
# print(my_list1 == [1,2,3,4,5])

#37 Ichki roʻyxat yaratish: Har bir kichik roʻyxatda asl roʻyxatdagi 
# elementlarning belgilangan sonini oʻz ichiga oluvchi quyi roʻyxatlar mavjud boʻlgan yangi roʻyxat yarating.
# my_list = [1,2,3]
# my_list1 = [[1,2,3],[1,2,3,4],[1,2,3,4,5]]
# my_list.extend(my_list1)
# print(my_list)

#38 Noyob elementlarni tartibda oling: ro'yxatni hisobga olgan holda,
#  asl tartibni saqlagan holda noyob elementlarni o'z ichiga olgan yangi ro'yxat yarating.
# my_list = ['1','2','3']
# my_list.append('a')
# my_list.append(1)
# my_list.append(8)
# my_list.append("olcha")
# print(my_list)
