def add(x, y) :
    return x+y
def subtract(x, y) :
    return x-y
def multiply(x, y) :
    return x*y
def divide(x, y) :
    return x/y

print("pilih operasi.")
print("1. jumlah")
print("2. kurang")
print("3. kali")
print("4. bagi")

choice = input("masukan pilihan(1/2/3/4) : ")
num1 = int(input("masukan bilangan pertama: "))
num2 = int(input("masukan bilangan kedua: "))

if choice == '1':
        print(num1,"+",num2,"=",add(num1,num2))

elif choice == '2':
        print(num1,"-",num2,"=",subtract(num1,num2))

elif choice == '3':
        print(num1,"*",num2,"=",multiply(num1,num2))

elif choice == '4':
        print(num1,"/",num2,"=",divide(num1,num2))

else:
        print("input salah")
