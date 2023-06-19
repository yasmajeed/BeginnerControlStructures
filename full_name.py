'''User asked to input first_name, if nothing is entered user prompted to type name again. However,
in this case my code also prompts user to type there surname. How can I code it so the user has 
to type there name before moving on to type there surname? Likewise, how can I code so 
the user has to enter a valid surname before concluding on the final else statement?

I feel my code works well when I do as it says, for example if I type my name, Yasmeen, it 
then it asks for my surname, Majeed and then executes the final elif statement "Thank 
you for entering your full name.." etc.

Im also not sure how to fix this, my code never goes to the else statement! 

Please advise, I would really like to improve this code after having it reviewed
'''  
first_name = input("Enter your first name: ")
if len(first_name) == 0:
    print("You have not entered anything, please type your name")

elif len(first_name) >2:
    print ("Great, now we need your surname")

surname = input("Enter your surname: ")
if len(surname) == 0:
    print("You have not entered anything, please type your surname")

elif len(surname) >2:
    print(f"Thank you for entering your full name: {first_name} {surname}")

else:
    ("Sorry, you can not proceed until you enter your full name")



            


