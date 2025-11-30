no_of_thoughts = int(input("How many thoughts do you want to store? "))
thoughts = []

for i in range(no_of_thoughts):
    thoughts.append(input("Your thought: ")) 
    b = i + 1

    if i == 0:
        with open("Example.txt", "w") as file: 
            file.write(f"{b} {thoughts[i]}\n")
    else:
        with open("Example.txt", "a") as file:
            file.write(f"{b} {thoughts[i]}\n")

with open("Example.txt", "r") as file:
    example = file.read()
    print(example)



