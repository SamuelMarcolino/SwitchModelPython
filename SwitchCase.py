#test of improv switch case
def menu ():
    print("Enter the desired option: \n 1- C° to F° \n 2- F° to C° \n 3- Lightning distance \n 4- How close to light speed(km) \n 5- How close to light speed(mph) \n 9- Quit program")
    option = int(input())
    print(f'You have selected option {option}! \n' )
    if option == 1 :
        print("This will help you with the conversion from Celcius to Farenheit.")
        a = float(input("Enter the Celcius value: "))
        total = (a *1.8) + 32
        print(f'The temperature in Farenheit is {round(total,2)} \n')
        menu()
    elif option == 2:
        print("This will help you with the conversion from Celcius to Farenheit.")    
        a = float(input("Enter the Farenheit value: "))
        total = (a - 32) * 0.5556
        print(f'The temperature in Celcius is {round(total,3)} \n')
        menu()
    elif option == 3:
        print("This will help you find out how far a lightning struck from you.")
        a = float(input("Enter how long till you hear the sound: "))
        total = a * 343
        print(f'The lightning was {round(total,3)}m away from you!')
        menu()
    elif option == 4:
        print("This will help you know how many % you are from the speed of light, using km/h as base")
        a = float(input("Enter your speed in km/h: "))
        b = 1080000000
        c = b/100
        total = float(a/c)
        print(f'You are at {"%.7f"%total}% of the speed of light')
        menu()
    elif option == 5:
        print("This will help you know how many % you are from the speed of light, using mph as base")
        a = float(input("Enter your speed in km/h: "))
        b = 669600000
        c = b/100
        total = float(a/c)
        print(f'You are at {"%.8f"%total}% of the speed of light')
        menu()
    elif option == 9:
        print('Application closed.')
    else:
        print('Invalid option. \n')
        menu()
menu()