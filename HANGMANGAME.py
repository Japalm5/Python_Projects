#  HANGMAN GAME

HANGMAN = "HANGMAN"
count = 0                                       # tracks wrong guesses to close while loop and notify loss
allowed_letters = "abcdefghijklmnopqrstuvwxyz"  # tracks if letters have been used before
number = 0
special_word = "0"
switch = 0

while switch == 0:
    switch = 1
    special_word = input("what is the word? ")      # word to guess, changes throughout program
    special_word = special_word.lower()
    print("\n"*20)
    for letter in special_word:
        if letter not in allowed_letters:
            print("please do not include spaces or special characters")
            switch = 0

length = len(special_word)                      # length of provided word to populate solution length
solution = "_" * length                         # shows what found characters are


while solution.__contains__("_") and count < 7:
    GUESS = input("what letter do you want to guess? ")
    GUESS = GUESS.lower()
    match = 0
    if allowed_letters.__contains__(GUESS):
        allowed_letters = allowed_letters.replace(GUESS, '*')
        number = special_word.count(GUESS)
        for CHARACTER in special_word:
            loopCounter = 0
            if CHARACTER == GUESS:
                for x in special_word:
                    if x == GUESS:
                        bs = list(solution)
                        bs[loopCounter] = GUESS
                        solution = "".join(bs)
                        match = 1
                    loopCounter += 1
        print("'{}' was found {} times!".format(GUESS, number))
        print(solution)
        print("Select one of the following letters: {}".format(allowed_letters))

        if match == 0:
            print("sorry, {} was not found.".format(GUESS))
            count += 1
            print(HANGMAN[0:count])

    else:
        count += 1
        print("Sorry, {} is an invalid character".format(GUESS))
        print(HANGMAN[0:count])

if count == 7:
    print("HANGMAN, Try again")
elif solution == special_word:
    print("Congrats, you win!")
else:
    print("error")
