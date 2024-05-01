# Magic 8 Ball 🎱
# Codédex

Import random
Question = input("Question:    ")
Random_number = random.randint(1, 9)

If random_number == 1:
   answer = "Yes - Definitely"
Elif random_number == 2:
   answer = "It is decidedly so"
Elif random_number == 3:
   answer = "Without a doubt"
Elif random_number == 4:
   answer = "Reply hazy, try again"
Elif random_number == 5:
   answer = "Ask again later"
Elif random_number == 6:
   answer = "Better not tell you now"
Elif random_number == 7:
   answer = "My sources say no"
Elif random_number == 8:
   answer = "Outlook not so Good"
Elif random_number == 9:
   answer = "Very Doubtful"
Else:
   answer = "Error"

Print("Magic 8 Ball:  " + answer)
