


import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list=['keyboard', 'river', 'grass', 'elephant', 'music', 'stone', 'car', 'keyboard', 'sun', 'river', 
 'sun', 'notebook', 'pencil', 'sun', 'music', 'car', 'mouse', 'lamp', 'banana', 'elephant', 
 'grass', 'milk', 'ocean', 'tea', 'moon', 'tiger', 'river', 'sun', 'keyboard', 'music', 'dog', 
 'bottle', 'keyboard', 'cheese', 'sun', 'ocean', 'sky', 'sky', 'keyboard', 'stone', 'notebook', 
 'lion', 'lamp', 'river', 'stone', 'bottle', 'door', 'lamp', 'table', 'building']

print(logo)
lives = 6
chosen_word = random.choice(word_list)



placeholder = ""


word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)
game_over = False
correct_letters = []





while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guesses the letter {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"letter '{letter}' is not in the word")

        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word}!YOU LOSE**********************")
            print(chosen_word)

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
