Famly_members = ["Andria", "Giorgi", "Niko", "Ksenia"]


for i in range(len(Famly_members)):
        print(f"{i + 1}. {Famly_members[i]}")



numbers = [1,2,3,4,5,6,7,8,9,10]

first = numbers[0]
print("first element: ", first)

last = numbers[-1]
print("last element: ", last)





numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


for i in range(0, len(numbers), 2):
    numbers[i] = 1

print(numbers)




name = input("What Is Ur Name: ")

surname = input("What Is Ur Surname: ")

age = input("What Is Ur Age: ")

location = input("Where Do You Live: ")

email = input("What Is Ur Email: ")


all_thogether = [name, surname, age, location, email]

print(all_thogether)




Surname = "Kamenski"

for i in range(len(Surname)):
    print(Surname[i])