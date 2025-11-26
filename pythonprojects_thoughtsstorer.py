no_of_thought = int(input("How many thoughts do you want to store? "))
thoughts = []

for i in range(no_of_thought):
    thoughts.append(input("Your thought: ")) 

for thought_number in range(no_of_thought):
    if thought_number == 0:
        with open("Example.txt", "w") as file: 
            file.write(thoughts[thought_number] + "\n")
    else:
        with open("Example.txt", "a") as file:
            file.write(thoughts[thought_number] + "\n")

with open("Example.txt", "r") as file:
    example = file.read()
    print(example)



