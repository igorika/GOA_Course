num1 = int(input("Pleace Enter Quantity Numbers Of How Many You Want To Enter: "))

numbers = []

for i in range(num1):
    num = int(input("Pleace Enter Number " + str(i+1) +": "))

numbers.append(num)
print(numbers)

print(len(numbers))





start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

numbers1 = []

for i in range(start, end):
       numbers1.append(i)

print(numbers1)


print(max(numbers1))
print(min(numbers1))
print(sum(numbers1))




numbers = []

for i in range(1, 10):
    numbers.append(i)

print(len(numbers))


