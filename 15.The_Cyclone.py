#The Cyclone

Height = int(input("What is your height (cm)? "))
Credits = int(input("How many credits do you have? "))

If height >= 137 and credits >= 10:
   Print("Enjoy the ride!")
Elif height < 137 and credits >= 10: 
   Print("You are no tall enough to ride.")
Elif credits < 10 and height >= 137:
   Print("You don't have enough credits to ride.")
Else:
   Print("You are not tall enough for this ride, nor do you have enough credits.")
