x = int(input('chislo: '))
sum = 0
sum = sum + (x % 10)
x = x//10
sum = sum + (x % 10)
x = x//10
sum = sum + (x % 10)
x = x//10

print(sum)

