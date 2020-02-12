
import random




choice_list = ['rock','scissors','paper']

computer_input = random.choice(choice_list)

user_input = (input("enter your choice:  "))



if (computer_input=="rock" and user_input=="scissors"):
    print("computer choice:  "+computer_input)
    print("you loose")
elif(computer_input =="paper" and user_input=="rock"):
    print("computer choice:  " + computer_input)
    print("you loose")
elif(computer_input=="scissors" and user_input=="paper"):
    print("computer choice:  " + computer_input)
    print("you loose")

elif(computer_input == "rock" and user_input == "rock"):
    print("computer choice:  " + computer_input)
    print("you draw")
elif (computer_input == "paper" and user_input == "paper"):
    print("computer choice:  " + computer_input)
    print("you draw")
elif (computer_input == "scissors" and user_input == "scissors"):
    print("computer choice:  " + computer_input)
    print("you draw")


else:
    if(user_input != 'scissors' and user_input!='rock' and user_input!='paper'):
        print("you entered wrong word please check spelling")
    else:
        print("computer choice:  " + computer_input)
        print("you win")
