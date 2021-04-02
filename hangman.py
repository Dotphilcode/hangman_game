import random

print("H A N G M A N")

while True:
    menu_question = input('Type "play" to play the game, "exit" to quit: ')

    if menu_question == "play":
        hidden_word = ''
        attempt = 8
        simple_list = []

        words = ['python', 'java', 'kotlin', 'javascript']
        chosen_word = random.choice(words)
        word_list = list(chosen_word)

        for char in chosen_word:
            hidden_word += '-'
        hidden_list = list(hidden_word)

        while attempt > 0:
            print()
            print(hidden_word)
            if hidden_word == chosen_word:
                print("""You guessed the word!
        You survived!""")
                break
            else:
                guess_letter = input("Input a letter: ")
                simple_list.append(guess_letter)
                if len(guess_letter) != 1:
                    print("You should input a single letter")
                elif guess_letter.islower() is False:
                    print("Please enter a lowercase English letter")
                elif guess_letter in hidden_list or guess_letter in simple_list[:(len(simple_list) - 1)]:
                    print("You've already guessed this letter")
                elif guess_letter not in chosen_word:
                    print("That letter doesn't appear in the word")
                    attempt -= 1
                elif guess_letter in chosen_word:
                    for j in range(len(word_list)):
                        if guess_letter == word_list[j]:
                            hidden_list.insert(j, guess_letter)
                            del hidden_list[j + 1]
                            hidden_word = ''.join(hidden_list)
        else:
            print("You lost!")
    elif menu_question == "exit":
        break
    else:
        continue
