import random

def get_word():
    words = ["man","forest","zebra","python","ostrich"]
    return random.choice(words)

def play_again():
    answer = input("Would you like to play again?").lower()
    if answer == "y" or answer == "yes":
        play_game()
    else:
        pass
def play_game():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    word = get_word()
    letters_guessed = []
    tries = 10
    guessed = False
    print("The word contains", len(word), "letters")
    print(len(word)* "*")

    while guessed == False and tries > 0 :
        print("You have " + str(tries) + " tries")
        guess = input("Please enter one letter or the word").lower()

        #1 if the input is one letter
        if len(guess) == 1:
            if guess not in alphabet:
                print("Please enter a valid letter")
            elif guess not in word:
                print("Wrong guess,letter not in the word")
                letters_guessed.append(guess)
                tries -= 1
            elif guess in letters_guessed:
                print("You have already guessed that letter")
            elif guess in word:
                print("Well done,that letter exists in the word")
                letters_guessed.append(guess)
            else:
                print("ok")

        #2 user input is full word
        elif len(guess) == len(word):
            if(guess == word):
                print("Congratulations!,you have guessed the word.")
                guessed =True
            else:
                print("Sorry,wrong guess")
                tries -= 1

        #3 user inputs wrong input
        else:
            print("Length of your guess is not same as length of the word ")


        status = ""
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else :
                    status += "*"
            print(status)

        if status == word:
            print("Well done, you have guessed the word correctly!")
            guessed = True

        elif tries == 0:
            print("You have no tries left and you have not guessed the word yet.")

    play_again()

play_game()