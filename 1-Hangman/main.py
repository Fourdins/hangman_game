import random

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list #import word list
lives = 6

from hangman_art import logo #import logo
print(logo)

chosen_word = random.choice(word_list) #choose a random word from word_list imported from hangman_words
print(chosen_word)

placeholder = ""                        #create a placeholder
word_length = len(chosen_word)          #get the chosen words lenght
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)  #print the word to guess

game_over = False                       #condition for while loop false
correct_letters = []                    #variable to store the guessed letters

while not game_over:                    #while game over is false

    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()                                               #get the user's guess

    if guess in correct_letters:                                                            #if users guess a word he already guessed let them know and don't make them lose a life
        print(f"You already guessed {guess}")
        lives = lives

    display = ""                                                                            #print the word they're guessing

    for letter in chosen_word:                                                              #for loop to guess the word
        if letter == guess:
            display += letter
            correct_letters.append(guess)                                                   #store the guessed letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")             #make user lose life is guessed wrong

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:                                                                      #if lives end stop the game
            game_over = True

            print(f"***********************YOU LOSE**********************")

    if "_" not in display:                                                                  #if user guessed the word stop the game
        game_over = True
        print("****************************YOU WIN****************************")

    from hangman_art import stages
    print(stages[lives])