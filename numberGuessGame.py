import random, easygui

secret = random.randint(1, 99)
guess = 0
num_tries = 0
easygui.msgbox("Lookie here, whatcha doing? Know what? "
               "I don't care. I am not letting you go until you pass my "
               "test\nI am thinking of a number between 1 and 99, guess what the number is,"
               " and I will give you a"
               " cookie and let you go.\nGuess it wrong at the end, and you're stuck with me, hahahahaha."
               " Give it a shot, hotshot! Oh, you get 7 tries by the way, byeeee!")
while guess != secret and num_tries < 7:
    guess = easygui.integerbox("What is your guess, bruhhhh? You have "+ str(7-num_tries)+" tries left")
    if (guess > secret):
        easygui.msgbox(str(guess) + " is a lil too high, ye scurvy lil turd!")
    elif (guess < secret):
        easygui.msgbox("Come on now, " + str(guess) + " is too low, don't ya think?")
    num_tries += 1
if (guess == secret):
    easygui.msgbox("Dang, you figured it out, here is your cookie. Now get out!")
else:
    easygui.msgbox("You a lil slow, eh? Welp, you're"
                   " stuck with me coz you lost fam! The number was " + str(secret))
