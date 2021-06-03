import time
def q1():
    reply = input("What is the date (mm/dd/yy): ")
    if reply == "06/03/21" or reply == "6/3/21":
        print("Correct!")
        q2()
    else:
        print("Incorrect")
        q1()

def q2():
    reply = input("What is the sum of the combination lock numbers: ")
    if reply == "10":
        print("Correct!")
        q3()
    else:
        print("Incorrect")
        q2()

def q3():
    print("Refer to the image provided")
    reply = input("Targeting system: what are the coordinates for the grassy knoll (#, #): ")
    if reply == "#, #": #TODO
        print("Correct!")
        q4()
    else:
        print("Incorrect")
        q3()

def q4():
    reply = input("Launch Authorization: what is the name of the TASC President: ")
    if reply == "Solomon" or reply =="Solomon Cornell":
        print("Correct!")
        q5()
    else:
        print("Incorrect")
        q4()

def q5():
    reply = input("Enter authorization code (starts with TIDE-LAUNCH, hidden somewhere in the room): ")
    if reply == "TIDE-LAUNCH##########" or reply == "#############": #TODO
        print("Correct!")
        q6()
    else:
        print("Incorrect")
        q5()

def q6():
    print("Go to this link: http://bit.ly/escape-room-2021")
    time.sleep(10)
    print("Just kidding :)")
    while True:
        if input("Ready to procede Y/N ") == "Y" or "y":
            launch()


def launch():
    def countdown(t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        print('Closing airlock')
        time.sleep(2)
        print("Imposter, reveal yourself")
        time.sleep(3)
        print("Game finished")
        exit()

    print("Preparing to launch. Vote someone to be launched to space and to save earth, but beware: if you send the imposters, you will fail")

    countdown(90)

q1()