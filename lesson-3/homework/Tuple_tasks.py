#1 Count Occurrences: Given a tuple and an element, 
# find how many times the element appears in the tuple.
# t = (1,2,3,4,5,2,3,4,2,3,2,3,3)
# print('2lar soni',t.count(2),'ta')

#2 Max Element: From a given tuple, determine the largest element.
# t = (1,5,8,13,99)
# print('eng katta elementi: ', max(t))

# #3 Min Element: From a given tuple, determine the smallest element.
# t = (1,5,8,13,99)
# print('eng kichik elementi: ', min(t))

#4 Check Element: Given a tuple and an element, check if the element is present in the tuple.
# t = (1,2,3,4,5,2,3,4,2,3,2,3,3)
# print(t.count(8)!=0)
# print(t.count(5)!=0)

#5 First Element: Access the first element of a tuple, considering what to return if the tuple is empty.
# Birinchi element:
#  Agar kortej bo'sh bo'lsa, nimani qaytarish kerakligini hisobga olib, kortejning birinchi elementiga kiring.
# t = (1,2)
# my_list = list(t)
# if bool(my_list)==False:
#     print('list bosh')
# elif bool(my_list)==True:
#     print('listning birinchi elementi:',my_list[0])





#6 Last Element: Access the last element of a tuple, considering what to return if the tuple is empty.
# Oxirgi element: 
# Agar kortej bo'sh bo'lsa, nimani qaytarish kerakligini hisobga olib, kortejning oxirgi elementiga kiring.
# t = (1,2)
# my_list = list(t)
# if bool(my_list)==False:
#     print('list bosh')
# elif bool(my_list)==True:
#     print('listning oxirgi elementi:',my_list[-1])

#7 Tuple Length: Determine the number of elements in the tuple.
# t = (1,2,3,4,5,2,3,4,2,3,2,3,3)
# print(len(t))

#8 Slice Tuple: Create a new tuple that contains only the first three elements of the original tuple.
# t = (1,5,8,13,99)
# print(t[0:3])

#9 Concatenate Tuples: Given two tuples, create a new tuple that combines both.
# t1 = ('a','b','c','d')
# t2 = (1,2,3,4)
# print(t1+t2)

#10 Tuple bo'sh yoki yo'qligini tekshiring: kortejda biron bir element mavjudligini aniqlang.
# t1 = (1,2,3)
# t2 = ()
# print(bool(t1))
# print(bool(t2))

#11 Elementning barcha indekslarini oling: 
# kortej va element berilgan bo'lsa, kortejdagi ushbu elementning barcha indekslarini toping.
# t = ('a','b','c','a','b','d','a')
# a = t.index('a',)
# b = t.index('a',a+1)
# c = t.index('a',b+1)
# print(' tupleda "a" elementi ',a,',',b,',',c, 'indexlarda joylashgan')

#12 Ikkinchi eng katta elementni toping: Berilgan kortejdan ikkinchi eng katta elementni toping.
# t = (1,5,8,13,99)
# tlist = list(t)
# a = max(tlist)
# tlist.remove(a)
# print(max(tlist))

#13 Ikkinchi eng kichik elementni toping: Berilgan kortejdan ikkinchi eng kichik elementni toping.
# t = (1,5,8,13,99)
# tlist = list(t)
# a = min(tlist)
# tlist.remove(a)
# print(min(tlist))

#14 Yagona element to'plamini yarating: bitta belgilangan elementni o'z ichiga olgan kortej yarating.
# print(tuple(range(3,4)))

#15 Convert List to Tuple: Given a list, create a tuple containing the same elements.
# my_list = [1,2,3,4,5,6,7,8]
# t = tuple(my_list)
# print(t)

#16 Tuple Saralangan yoki yo'qligini tekshiring:
#Kortej o'sish tartibida tartiblanganligini aniqlang va mantiqiy qiymatni qaytaring.
# t1 = (1,2,3,4,5,6,7,8,9,10)
# t2 = (4,5,6,7,3,2,1,9,10)
# t1list = list(t1)
# t2list = list(t2)
# print(t1list == sorted(t1list))
# print(t2list == sorted(t2list))



#17 Find Minimum of Subtuple: Given a tuple, find the minimum element of a specified subtuple.
# t = (1,2,3,(4,5,6),7)
# a = t[3]
# print(min(a))



#18 Find Maximum of Subtuple: Given a tuple, find the maximum element of a specified subtuple.
# t = (1,2,3,(4,5,6),7)
# a = t[3]
# print(max(a))

#19 Elementni qiymat bo'yicha olib tashlash: Kortej va elementni hisobga olgan holda, 
#ushbu elementning birinchi paydo bo'lishini olib tashlaydigan yangi kortej yarating.
# t = (1,2,3,4,5,2,3,4,2,3,2,3,3)
# tlist = list(t)
# a = tlist.index(4)
# tlist.remove(tlist[a])
# t1 = tuple(tlist)
# print(t1)

#20 Create Nested Tuple: Create a new tuple that contains subtuples,
#  where each subtuple contains specified elements from the original tuple.
# Nested kortej yaratish: Har bir subtuple asl kortejdan belgilangan elementlarni
#  o'z ichiga olgan pastki qatorlarni o'z ichiga olgan yangi kortej yarating.
# t = ((1,2),(3,4),(5,6))
# tlist = list(t)
# txlist = ((tlist[0],tlist[1]),(tlist[1],tlist[2]),(tlist[0],tlist[2]))
# tx = tuple(txlist)
# print(tx)

#21 Elementlarni takrorlash: 
# tuple va element berilgan bo'lsa, har bir element shuncha marta takrorlanadigan yangi tuple yarating.
# t = (1,2,3,4,5)
# print(t,'ushbu tupledagi elementlar nechta marta takrorlanishini kiriting')
# x = int(input("tanlagan soningiz tuple elentlari orasida bolsin: "))
# tlist = list(t)
# a = tlist.copy()
# atuple = tuple(a)
# print(t+atuple*x)

#22 Rang qatorini yaratish: Belgilangan diapazonda raqamlar majmuasini yarating (masalan, 1 dan 10 gacha).
# print(tuple(range(25,37)))

#23 Teskari kortej: Asl kortej elementlarini teskari tartibda o'z ichiga olgan yangi kortej yarating.
# t = (1,2,3,4,5,'a','b','c','d',6,7,8,9,10)
# tlist = list(t)
# tlist.reverse()
# print(tuple(tlist))

#24 Palindromni tekshiring: kortej berilgan bo'lsa, 
# kortej palindrom ekanligini tekshiring (xuddi shu narsani oldinga va orqaga o'qiydi).
# t1 = (1,2,3,4,5)
# t2 = (1,2,3,2,1)
# a = list(t1)
# b = list(t2)
# a.reverse()
# b.reverse()
# print(a == list(t1))
# print(b == list(t2))

#25 Noyob elementlarni oling: tupleni hisobga olgan holda, asl tartibni saqlab, 
# faqat noyob elementlarni o'z ichiga olgan yangi tuple yarating.
# Get Unique Elements: Given a tuple, create a new tuple that contains
#  only the unique elements while maintaining the original order.
# t = (1,2,3,4,5,6,7,'a',8,'b',9,'c',10,'d')
# tlist = list(t)
# orginallist = [tlist[7],tlist[9],tlist[11],tlist[13]]
# orginaltuple = tuple(orginallist)
# print(orginaltuple)



