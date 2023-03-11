import random
from hangman_guessing import word_list
from hangman_life import lives
from hangman_life import game_name

#Store score
class Leaderboard():
    player_score = 0
    executioner = 0

game_over = False

#game mech    
def LetterGuess(turns, word_list):
    #game setting
    random_word = random.choice(word_list).lower() #choose word
    print(random_word)
    blanks = '_' * len(random_word)
    #conditions
    try:
        while turns > 0:
            #guess
            guess = input('Guess a letter ').lower()
            if guess in random_word:
                #find letter in guess & replace
                for i in range(len(random_word)): # Replace blanks with correctly guessed letters.
                    if random_word[i] in guess:
                        blanks = blanks[:i] + random_word[i] + blanks[i+1:]      
                print(blanks)
                #message
                if ("_") not in blanks:
                    game_over = True
                    print("You are a winner, congratulations!")
                    print(f"The word was {random_word}")
                    Leaderboard.player_score +=1
                    break
                print(f"Well done, you have {turns} lives left")

            elif guess not in random_word:
                turns -= 1
                print(blanks)
                print(lives[turns])
                if turns == 0:
                    game_over = True
                    print("Game over")
                    print(f"The word was {random_word}")
                    Leaderboard.executioner +=1
                    break
                print(f"Wrong, think carefully you have {turns} lives left") 
    except ValueError:
        print("Only letters are allowed, don't get too clever!")



#define levels
def easy():
    print("You have 7 lives to guess")
    print("Sounds easy enough? Let's see you do it!")
    LetterGuess(7,word_list)

def medium():
    print("You have 6 lives to guess")
    print("Sounds easy enough? Let's see you do it!")
    LetterGuess(6,word_list)

def hard():
    print("You have 5 lives to guess")
    print("Sounds easy enough? Let's see you do it!")
    LetterGuess(5,word_list)


#try again & leaderboard
def try_again():
    print(f"You - {Leaderboard.player_score}")
    print(f"Executioner - {Leaderboard.executioner}")
    again = input("Do you want to play again? Yes / No ")
    if again.upper() == 'YES' :
        welcome()
    elif again.upper() == "NO" : 
        print("Thanks for playing ")
        if Leaderboard.executioner > Leaderboard.player_score:
            print(f"The executioner beat you by {Leaderboard.executioner - Leaderboard.player_score} points")
        elif Leaderboard.player_score > Leaderboard.executioner:
            print(f"You won by {Leaderboard.player_score - Leaderboard.executioner} points")
        elif Leaderboard.player_score == Leaderboard.executioner:
            print("Even game! Maybe next time!")
    else:
        print("Say that again...Yes or no? ")
        try_again()

# Choose level
def welcome():
    print("Let's play hangman!")
    print(game_name)
    print("You need to guess the word before the man is hung")
    difficulty = input("Choose your level - Easy, Medium and Hard? ")
    if difficulty.upper() == "EASY":
        easy()
        try_again()
    elif difficulty.upper() == "MEDIUM":
        medium()
        try_again()
    elif difficulty.upper() == "HARD":
        hard()
        try_again()
    else:
        print("That's not a level! Try again!")
        welcome()
welcome()






