a = int(input("Ведите кол-во элементов в списке "))
b = []
for i in range(1,1+a):
    print("Пожалуйста, введите " ,i, " элемент")
    c = int(input())
    b.append(c)
print("Все нечетные числа: ")
for i in b:
    if i%2 != 0:
        print(i)
        
    
