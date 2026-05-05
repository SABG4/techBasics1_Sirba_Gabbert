import time
import datetime
#converting 'today' into a string with the format (YYYY-MM-DD)
today = datetime.date.today()
today_str= today.strftime("%Y-%m-%d")

#introduction to the 'game', fundament
print("Welcome to \"The Birthday Planner\" 🎉🎂🎁","--- 🗓 Today is the", today)
time.sleep(3)
name = input("What's your name? ")
time.sleep(1)
print("Hello", name)
time.sleep(1)
#assuring with .strip, that inputs can contain spaces and still be valid
birthday = input('When is your birthday this year? Please type in this format!: YYYY-MM-DD').strip()

#conditional statement 1, version without while-loop
##assuring that the input uses only digits and "-"(-> further improvement would imply assuring that input follows the specific format
if birthday.replace("-", "").isdigit() and birthday == today_str:
    print(f"Happppy Birthday {name} \n I hope you are having a wonderful day 🥳🎂🎈")
else:
    print("Nice, then let's plan your birthday 😉")


    #brithday planning
    time.sleep(1)
    ##step 1: guests
    print("1. We will start with your guests 👥:")
    time.sleep(2)

    ##while loop until user enters a valid number below 100
    while True:
        guests = input("How many people do you want to invite?")

        if guests.isdigit() and int(guests) <100:
            guests = int(guests)
            if guests in range(1,11):
                print("Nice, it will be a cozy atmosphere and probably 1 cake is enough🎂 ;)")
            elif guests in range(11,26):
                print("Great, you will need a bit more space and probably 2 to 3 cakes 🎂🎂")
            elif guests in range(26,100):
                print("How cool, that's a lot of people. You will need quite some space and probably more than 4 cakes 🎂🎂🎂🎂")
            break
        else:
            print("This is not a valid number format, please try again")

    ###step2: some inspiration for locations
    time.sleep(2)
    print("2. Let's continue with the location 📍 ")
    time.sleep(1)

    ###while loop until user enters a valid answer
    ###again reassuring that the user's input can contain spaces and still be valid
    while True:
        weather = input("What will the weather be like on your birthday?").strip()
        if str(weather) == "cold" or str(weather) =="warm" or str(weather) == "hot":
            weather = str(weather)
            if weather == "cold":
                print("Then these are perfect options as locations❄️: \n • at home \n • restaurant \n • café \n • cinema \n • ...  ")
            elif weather == "warm":
                print("Then these are perfect options as locations🌤: \n • park \n • forest \n • ice café \n • amusement park \n • ...  ")
            elif weather == "hot":
                print("Then these are perfect options as locations☀️: \n • sea \n • swimming pool \n • stand up paddling \n • inside in a cool room \n • ...  ")
            break
        else:
            print("This is not a valid answer, please re-enter (cold, warm or hot)")

####step3: food inspiration on basis of favourite number
time.sleep(4)
print("3. You can't decide on your food, no worries here is some inspiration🍜:")
time.sleep(1)
food = input("Choose a number from 1-10 ?")
time.sleep(2)


if int(food) <4:
    print("The perfect food for your birthday party: Quick and simple:🌮 fingerfood")
elif int(food) in range(4,7):
    print("Your choice for the day:🍕 fast food (pizza, burger, fries)🍔")
elif int(food) in range (7,11):
    print("What about something really healthy (salad, different fruit)🥗🍉 ?")


#####step4:invitation letter:
time.sleep(3)
invitation = input("4.Last, but not least: Would you like a short invitation text that you can send to your guests?")

if str(invitation).lower() == "yes":
    name_guest = input("What is your guest's name?")
    print(f"Dear {name_guest}, I would like to invite you to my birthday party on the {birthday}. The exact time and location will be announced later. I would be thrilled if you could come:)). Yours {name}🌸")
else:
    print("Okay, you are all set, I wish you a wonderful birthday party🎊 ")
time.sleep(4)
print("Thank you for playing the birthday planning game🎂🎊  ")
