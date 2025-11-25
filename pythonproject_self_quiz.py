total_score = 0

list_question1 = ["Is buhari dead?", "yes", "no"]
list_question2 = ["Is FUTMinna the name of a school?", "yes", "no"]
list_question3 = ["can you solve Mathematics?", "yes", "no"]
list_question4 = ["Can you code in C?", "yes", "no"]

while True:
   
   print(list_question1[0])
   response = input("your answer: ")

   if response == list_question1[1]:
      total_score += 1
    
   print(list_question2[0])
   response = input("your answer: ")

   if response == list_question2[1]:
      total_score += 1

   print(list_question3[0])
   response = input("your answer: ")

   if response == list_question3[1]:
      total_score += 1
      
   print(list_question4[0])
   response = input("your answer: ")

   if response == list_question4[1]:
      total_score += 1

   break
   
print(f"Your total score is: {total_score}/4. Congrats")