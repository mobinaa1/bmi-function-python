b=[]
def bmi_calculater():
    h = float(input("enter your height(m):"))
    w = int(input("enter your weight(kg): "))
    bmi = w /(h**2)
    if bmi < 18.5:
        print("you are underweight")
    elif bmi<25:
        print("you are normal")
    elif bmi <30:
        print("you are overweight")
    else:
        print("you are fat")
    return bmi
print(bmi_calculater())


