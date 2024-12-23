#1
  
# a= float(input("yaxlitlanadigan sonni kiriting: a= "))
# print(f"{a:.2f}")


#2

# a = int(input("birinchi sonni kiriting: a="))
# b = int(input("ikkinchi sonni kiriting: b="))
# c = int(input("uchinchi sonni kiriting: c="))

# min_number = min(a,b,c)
# max_number = max(a,b,c)
# print("eng kichigi:", min_number)
# print("eng kattasi: ", max_number)



#3
# l = float(input("masofani kiriting: L(km)= "))
# l_m = l*1000
# l_cm = l*100000

# print("Bu masofa santimetrlarda", l_cm, " cm ga va metrlarda", l_m, "m ga teng")

#4
# a = int(input('a='))
# b = int(input("b="))
# c=a//b 
# d=a%b 
# print(c,"dan yetib",d,"qoldiq qoldi")

#5
# t = float(input("Temperaturani kiriting: t(C)= "))
# F=t*9/5+32
# print(F,"Farangeyt")

#6
# n = input("Raqamni kiriting: n = ")
# oxirgi_raqam = n[-1]
# print("oxirgi raqam", oxirgi_raqam)

#7
# a = int(input("sonni kiriting: "))
# print("Toq"*(a%2) + "Juft"*(1-a%2))

#8
# ism = input("Ismingizni kiriting: ")
# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh = 2024-yil
# print("Hurmatli", ism, "siz",yosh,"yoshdasiz!")

#9
# txt = 'LMaasleitbtui'
# car1 = txt[1] + txt[2] + txt[5] + txt[7] + txt[9] + txt[11]
# car2 = txt[0] + txt[3] + txt[4] + txt[6] + txt[8] + txt[10] + txt[12]
# print(car1)
# print(car2)

#10
# word = input("ism familiyangizni kiriting: ")
# print(len(word))
# print(word.upper())
# print(word.lower())
# print(word.title())
# print(word.capitalize())
# print(word[::-1])


# 11
# print("Men olmani yaxshi ko'raman")
# meva = input(" siz yoqtiradigan meva nomini kiriting:")
# print('Men',meva+"larni yaxshi ko'raman")

# 12
# satr = input("Satrni kiriting:")
# print("birinchi belgi:", satr[0])
# print("oxirgi belgi:", satr[-1])


# 13
# satr = input("satrni kiriting:")
# print(satr[::-1])


# 14
# nom = input("Foydalanuvchi nomini kiriting: ")
# parol = input("parolni kiriting: ")
# if nom!=0 and parol==0:
#     print("parolni kiritishni unutdingiz!")
# elif nom!=0 and parol!=0:
#     print("sizning so'rovnomangiz qabul qilindi!")
# else:
#     print("Ma'lumotlarni toliq kiriting!")

# 15
# a = int(input("a="))
# b = int(input("b="))
# if a==b:
#     print("raqamlar teng")
# else:
#     print("raqamlar teng emas")   


# 16
# a = int(input("a="))
# if 1-a%2 and a>0:
#     print("bu son juft va musbat")
# else:
#     print("biz xohlagan son emas")

# 17
# a = int(input("a="))
# b = int(input("b="))
# c = int(input("c="))
# if a==b==c:
#     print("uchala son teng")
# else:
#     print("bu sonlar teng emas")

# 18
# a = int(input("sonni kiriting:"))
# if a%3==0 and a%5==0:
#     print("bu son 3 ga va 5 ga bolinadi")
# else:
#     print("bu son 15 ga bolinmaydi")


# 19
# x = float(input("x="))
# y = float(input("y= "))
# if x+y>50:
#     print('x+y>50')
# else:
#     print("x+y<50")