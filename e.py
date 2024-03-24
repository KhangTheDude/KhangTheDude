# print("bai 1")
# a = 0
# for i in range(0,100):
#     if a % 3 == 0:
#         print(a)
#     a = a + 1

# print("bai 2")
# a = 0
# for i in range(0,50):
#     if a % 2 == 0:
#         print(a)
#     a = a + 1

# name = str(input("Type username here: "))
# if name == "admin":
#     password = input("Type password here: ")
#     if password == "123456@Abc":
#         print("wellcome")
#     else:
#         print("Wrong password")
# else:
#     print("Wrong username")

# name = str(input("Type username here: "))
# if name == "admin":
#     password = input("Type password here: ")
#     if password == "123456@Abc":
#         print("wellcome")
#     else:
#         print("Wrong password")
# else:
#     print("Wrong username")

# name = str(input("Type username here: "))
# password = input("Type password here: ")
# if name == "admin" and password == "123456@Abc":
#     print("Wellcome")
# else:
#     print("Wrong username and password")
num1 = -1
num2 = -1
num3 = -1
while num1 > 10 or num1 < 0 or num2 > 10 or num2 < 0 or num3 > 10 or num3 < 0:
    num1 = int(input("Toan: "))
    num2 = int(input("Van: "))
    num3 = int(input("Anh: "))
TB = num1 + num2 + num3
if TB < 5:
    print("Ko dat")
elif TB >= 5 and TB < 7:
    print("Dat")
elif TB >= 7 and TB < 8:
    print("Kha")
elif TB >= 8:
    print("Tot")

mass = float(input("Mass ( In kilograms ) : "))
height = float(input("Height ( In meters ) : "))
BMI = mass / (height * 2)
if BMI < 16:
   print("Gay Cap Do III")
if BMI > 15 and BMI < 17:
   print("Gay Cap Do II")
if BMI > 16 and BMI < 18.5:
   print("Gay Cap Do I")
if BMI > 17.5 and BMI < 25:
   print("Binh Thuong")
if BMI > 24 and BMI < 30:
   print("Beo Phi Cap Do I")
if BMI > 34 and BMI < 40:
   print("Beo Phi Cap Do II")
if BMI > 40:
   print("Beo Phi Cap Do III")