#user input
def  user_input():
    weight = float(input("Enter your weight (kg) :"))
    height = float(input("Enter your height (m) : "))
    return weight , height

def cal_bmi(weight , height):
    bmi_calculator = (weight // height ** 2)
    return bmi_calculator

def get_bmi_result(bmi):

    print(f"bmi : {bmi}\nresult:")

    if bmi < 18.5:

        print("Under Weight")

    elif 18.5 <= bmi < 25:

        print("Normal")

    elif 25 <= bmi < 30:

        print("Over Weight")

    elif 30 <= bmi < 35:

        print("Obese")

    else:

        print("Extremely Obese")


def main():

    weight,height = user_input()
    bmi = cal_bmi(weight , height)
    get_bmi_result(bmi)


if __name__ == "__main__":

    main()

    