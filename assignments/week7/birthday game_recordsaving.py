# Birthday Planning Game
# This is a small birthday game, where users get to plan their birthday (guests, location, food & invitation letters)

import time
import datetime

# constants
DEBUG = True

TODAY = datetime.date.today()  # converting 'today' into a string with the format (YYYY-MM-DD)
TODAY_STR = TODAY.strftime("%Y-%m-%d")
WEATHER_OPTIONS = ["cold", "warm", "hot"]
FINAL_MESSAGE = "Thank you for playing the birthday planning game🎂🎊"


# functions
## record saving functions

def load_leaderboard (file= "leaderboard.txt"):
    try:
        with open(file, "r") as f:
            leaderboard = [line.strip() for line in f]
        return leaderboard

    except FileNotFoundError:
        print("The file leaderboard.txt was not found")

    return []

def save_leaderboard (data, file="leaderboard.txt"):
    with open(file, "w") as f:
        f.write ("\n".join(data))

def add_recordentry (username, timestamp, playtime, leaderboard):
    entry = f"{username} | {timestamp}| Time: {playtime:.2f}s"
    leaderboard.append(entry)

    return (leaderboard)


##function with while loop asking the user for the weather on their birthday and giving adequate location inspo
def weather():
    while True:
        user_weather = input("What will the weather be like on your birthday?").strip()
        if user_weather in WEATHER_OPTIONS:
            if user_weather == "cold":
                print(
                    "Then these are perfect options as locations❄️: \n • at home \n • restaurant \n • café \n • cinema \n • ...  ")
            elif user_weather == "warm":
                print(
                    "Then these are perfect options as locations🌤: \n • park \n • forest \n • ice café \n • amusement park \n • ...  ")
            elif user_weather == "hot":
                print(
                    "Then these are perfect options as locations☀️: \n • sea \n • swimming pool \n • stand up paddling \n • inside in a cool room \n • ...  ")
            break
        else:
            print("This is not a valid answer, please re-enter (cold, warm, hot)")


# here i defined a function for a custom invitation letter that uses the arguments: guest name, user name, birthday date
def custom_invitation(guest_name, birthday, username):
    return f"Dear {guest_name}, I would like to invite you to my birthday party on {birthday}. The exact time and location will be announced later. I would be thrilled if you could come:)). Yours, {username}🌸"


# main function
def main():
    start_time = time.time()

    # introduction to the 'game', fundament
    print("Welcome to \"The Birthday Planner\" 🎉🎂🎁", "--- 🗓 Today is the", TODAY)
    time.sleep(3)
    username = input("What's your name? ")
    time.sleep(1)
    print("Hello", username)
    time.sleep(1)


    #debug
    if DEBUG:
        print("The main body of the game will be skipped. This is the testing mode.")
        playtime = 10.0 #placeholder for testing
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        leaderboard = load_leaderboard()
        leaderboard = add_recordentry(username, timestamp, playtime, leaderboard)
        save_leaderboard(leaderboard)

    else:
        # assuring with .strip, that inputs can contain spaces and still be valid
        birthday = input('When is your birthday this year? Please type in this format!: YYYY-MM-DD').strip()
        # conditional statement 1, version without while-loop
        ##assuring that the input uses only digits and "-"(-> further improvement would imply assuring that input follows the specific format
        if birthday.replace("-", "").isdigit() and birthday == TODAY_STR:
            print(f"Happppy Birthday {username} \n I hope you are having a wonderful day 🥳🎂🎈")
        else:
            print("Nice, then let's plan your birthday 😉")

        # brithday planning
        time.sleep(1)
        ##step 1: guests
        print("1. We will start with your guests 👥:")
        time.sleep(2)

        ##while loop until user enters a valid number below 100
        while True:
            guests = input("How many people do you want to invite?")

            if guests.isdigit() and int(guests) < 100:
                guests = int(guests)
                if guests in range(1, 11):
                    print("Nice, it will be a cozy atmosphere and probably 1 cake is enough🎂 ;)")
                elif guests in range(11, 26):
                    print("Great, you will need a bit more space and probably 2 to 3 cakes 🎂🎂")
                elif guests in range(26, 100):
                    print(
                        "How cool, that's a lot of people. You will need quite some space and probably more than 4 cakes 🎂🎂🎂🎂")
                break
            else:
                print("This is not a valid number format, please try again")

        ###step2: some inspiration for locations
        time.sleep(2)
        print("2. Let's continue with the location 📍 ")
        time.sleep(1)
        # calling the weather function
        weather()

        ####step3: food inspiration on basis of favourite number
        time.sleep(4)
        print("3. You can't decide on your food, no worries here is some inspiration🍜:")
        time.sleep(1)

        while True:
            food = input("Choose a number from 1-10 ?")
            time.sleep(2)

            if int(food) < 4:
                print("The perfect food for your birthday party: Quick and simple:🌮 fingerfood")
                break
            elif int(food) in range(4, 7):
                print("Your choice for the day:🍕 fast food (pizza, burger, fries)🍔")
                break
            elif int(food) in range(7, 11):
                print("What about something really healthy (salad, different fruit)🥗🍉 ?")
                break

        #####step4:invitation letter:
        time.sleep(3)
        invitation = input(
            "4.Last, but not least: Would you like a short invitation text that you can send to your guests?")

        # calling the invitation letter function inside the condition
        if invitation.lower() == "yes":
            guest_name = input("What is your guest's name?")
            print(custom_invitation(guest_name, birthday, username))
        else:
            print("Okay, you are all set, I wish you a wonderful birthday party🎊")


        #stopping the time recording
        end_time = time.time()
        playtime = end_time - start_time

        #
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        leaderboard = load_leaderboard()
        leaderboard = add_recordentry(username, timestamp, playtime, leaderboard)
        save_leaderboard(leaderboard)

        time.sleep(4)
        print(FINAL_MESSAGE)

# -------------------------

if __name__ == "__main__":
    main()
