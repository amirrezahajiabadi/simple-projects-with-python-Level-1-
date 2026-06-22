import random

user_choices = ("rock" ,'paper' , 'scissor')

def get_user_input ():
    user = input("please enter your choice [\"rock\",\"paper\",\"scissor\"]:")
    while user not in user_choices:
         user = input("please enter your choice [\"rock\",\"paper\",\"scissor\"]:")
    return user

def pc_get_input ():
    pc = random.choice(user_choices)
    print(f"pc choice was :{pc}")
    return pc

def winner(user_choice , pc_choice):
    if user_choice == pc_choice :
        print ("Draw!")
    elif (user_choice == 'rock' and pc_choice == 'scissor') \
        or (user_choice == 'paper' and pc_choice == 'rock') \
        or (user_choice == 'scissor' and pc_choice == 'paper'):
        print ("user win!")
    else :
        print ("computer win!")


def main():
    user_input = get_user_input()
    pc_input = pc_get_input()
    winner(user_input, pc_input)
    print("end of program")



answer = 'y'
while answer == "y":
    main()
    answer = input("do you want to continue? (y/n):")