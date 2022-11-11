import re

def print_underscore(word):
    for letter in word:
        if letter == " ":
            print(" ", end = "")
        else:
            print("_", end = "")

def string_guess_with_underscore(word):
    visualization = ""
    for letter in word:
        if letter == " ":
            visualization += (" ")
        else:
            visualization += ("_")
    return visualization

""" def show_current_progress(guesses, hidden_word):
    current_visualization = string_guess_with_underscore(hidden_word)
    updated_visualization = ""
    x = 0 #guesses iterator
    if x < len(guesses):
        for letter in hidden_word:
            if guesses[x] == letter in hidden_word:
                updated_visualization = hidden_word.replace(guesses[x], letter)
            else:
                updated_visualization = hidden_word.replace(letter, "_")
        x += 1
    print(updated_visualization) """

def continue_playing(username):
    while True:
        continue_playing = input("\nWould you like to play again? Y(es) or N(o): ")
        if continue_playing.lower() == "y" or continue_playing.lower() == "yes":
            continue_playing = True
            break
        elif continue_playing.lower() == "n" or continue_playing.lower() == "no":
            end_game(username)
        else:
            print("\nInvalid selection {}, Try again.".format(username))
    return continue_playing

def end_game(username):
    print("\nSorry to see you go, come back soon {name}!\n".format(name = username))
    quit()

def show_current_progress(guesses, hidden_word, username):
    current_visualization = string_guess_with_underscore(hidden_word)
    updated_visualization = [x for x in current_visualization]
    x = 0 #guesses iterator
    if x < len(guesses):
        if guesses[x] in hidden_word:
            for letter in hidden_word:
                if x < len(guesses):
                    index_of_guess = hidden_word.find(guesses[x])
                    for letter in hidden_word:
                        if letter == guesses[x]:
                            updated_visualization[index_of_guess] = letter
                            index_of_guess = hidden_word.find(guesses[x],index_of_guess + 1)
                    x += 1
    updated_visualization = "".join(updated_visualization)
    # print(updated_visualization)
    return updated_visualization