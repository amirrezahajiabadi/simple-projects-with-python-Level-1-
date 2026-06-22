import random 

max_num = 10
min_num = 1



def generate_random_number ():
    return random.randint(min_num , max_num)



def get_user_input ():

    print (f"Your number should be between {min_num}-{max_num}")

    while True:
        try:
            user = int(input("Please enter your number :"))

        except ValueError:
            print ("Error : enter a valid number!")

        else:
            return user


def check_guessed_number(user_input,random_num):

    return user_input == random_num


def main():
    max_guess_number = 3
    rand_num = generate_random_number()
    print (f"Random number is {rand_num}")
    while max_guess_number>0:
        user_rand = get_user_input()
        if check_guessed_number(user_rand , rand_num):
            print ("That's great , you win!")
            break
        max_guess_number -=1
        print (f"guessed left {max_guess_number}")
    else:
        print ("that's not good , try again")


    
if __name__ == '__main__':
    main()
