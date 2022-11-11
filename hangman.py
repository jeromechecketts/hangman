
import random, hangman_fnc

# category_selected = {1: "Cities", 2: "Sports Figure", 3: "Presidents of the US", 4: "Car Model", 5: "Countries of the World", 6: "Random"}
username = input("\nPlease enter your name: ")
rules = """Welcome to Hangman {name}!

There are a few simple rules:
*     Select Category.  
*     You will have a total of 11 incorrect guesses before losing.""".format(name = username)
print("\n" + rules)

cities = ["Austin", "San Antonio", "Dallas", "Houston", "Denver", "Indianapolis", "Minneapolis", "Sacramento", "Las Vegas", "Seattle", "Boston", "San Franciso", "Chicago", "Portland", "New York", "Los Angeles"]
sports_figure = ["Michael Jordan", "Magic Johnson", "Larry Bird", "Kobe Bryant", "LeBron James", "Tom Brady", "Peyton Manning", "Joe Montana", "Ray Lewis", "Aaron Rogers"]
presidents_us = ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "Andrew Jackson", "Theodore Roosevelt", "Woodrow Wilson", "Herbert Hoover", "John F Kennedy", "Ronald Reagan", "George W Bush"]
sportscar_model = ["Corvette", "Mustang", "Viper", "Charger", "Challenger", "Camaro", "Supra", "Boxter", "Diablo", "NSX"]
countries_world = ["Costa Rica", "Panama", "Belgium", "Norway", "Bolivia", "Brazil", "Denmark", "Finland", "India", "Jamaica"]
random_choice = cities + sports_figure + presidents_us + sportscar_model + countries_world

continue_playing = True
while continue_playing == True:
    hidden_word = ""
    while not hidden_word:
        user_category = input("""\n\n\n Please select from one of the following categories: 
        1:  Cities
        2:  Sports Figure
        3:  Presidents of the US
        4:  Car Model
        5:  Countries of the World
        6:  Random

        7:  Quit \n\n""")
        if user_category == "1" or user_category.lower() == "cities":
            hidden_word = random.choice(cities).lower()
        elif user_category == "2" or user_category.lower() == "sports figure":
            hidden_word = random.choice(sports_figure).lower()
        elif user_category == "3" or user_category.lower() == "Presidents of the US":
            hidden_word = random.choice(presidents_us).lower()
        elif user_category == "4" or user_category.lower() == "car model":
            hidden_word = random.choice(sportscar_model).lower()
        elif user_category == "5" or user_category.lower() == "countries of the world":
            hidden_word = random.choice(countries_world).lower()
        elif user_category == "6" or user_category.lower() == "random":
            hidden_word = random.choice(random_choice).lower()
        elif user_category == "7" or user_category.lower() == "seven":
            hangman_fnc.end_game(username)
        else:
            print("\nPlease select from valid category.")
            continue
    # print(hidden_word.title()) #Remove at end, only shown so I know what word it is.
    hangman_fnc.print_underscore(hidden_word)
    print("\n\n")

    guess_list = set()
    correct_guesses = []
    incorrect_guesses = []
    shortest_rounds = 12
    current_rounds = 0
    parts = {1: "Base", 2: "Upper Riser", 3: "Cross Member", 4: "Noose Hanger", 5: "Angled Support", 6: "Head", 7: "Body", 8: "Left Arm", 9: "Right Arm", 10: "Left Leg", 11: "Right Leg"}
    parts_counter = 0
    incorrect_guesses_remaining = 11
    current_progress = ""
    continue_guessing = True
    while continue_guessing == True:
        print("""\nSelect 1 or 2 depending on what you would like to guess or 3 to quit: 
        1.  Letter
        2.  Whole word
        3.  Quit\n""")
        selection = input()
        if selection == "1":
            current_guess = input("\nPlease select a character to guess: \n\n").lower()
            current_rounds += 1
            if current_guess in hidden_word.lower():
                correct_guesses.append(current_guess)
                print("\nGood Job!!  You have guessed a letter in the hidden word\n")
                current_progress = hangman_fnc.show_current_progress(correct_guesses, hidden_word, username)
                print("\n" + current_progress)
                if "_" not in current_progress:
                    if current_rounds < shortest_rounds:
                        shortest_rounds = current_rounds
                        print("\nYou have the record for the least amount of guesses.  You solved the word in {} guesses".format(shortest_rounds))
                    else:
                        print("\nCongratulations you have guessed all the letters!!")
                        print("\nYou solved the word in {} guesses".format(current_rounds))
            if current_guess not in hidden_word and current_guess not in incorrect_guesses:
                parts_counter += 1
                incorrect_guesses.append(current_guess)
                incorrect_guesses_remaining -= 1
                current_progress = hangman_fnc.show_current_progress(correct_guesses, hidden_word, username)
                print("\n" + current_progress)
                if parts_counter < 11:
                    print("\nYou did NOT guess a correct letter you received {part}".format(part = parts[parts_counter]))
                    print("\nYou have {guesses} incorrect guesses remaining ".format(guesses = incorrect_guesses_remaining))
                else:
                    print("\nYou did NOT guess a correct letter you received {part}.  You LOST.".format(part = parts[parts_counter]))
                    hangman_fnc.continue_playing(username)
                    continue_guessing = False
            if current_guess not in guess_list:
                guess_list.add(current_guess)
                # print("Length of the hidden word is: " + str(len(hidden_word.replace(" ", ""))))
                # print("Length of the correct guesses is: " + str(len(correct_guesses)))
                print("\nLetters you have guessed:",guess_list) #Just temporarily here to see if guess list is being updated correctly.
                # print("correct_guess:",correct_guesses) #Just temporarily here to see if guess list is being updated correctly.
                # print("incorrect_guess:",incorrect_guesses) #Just temporarily here to see if guess list is being updated correctly.
                # if current_guess not in hidden_word.lower():
                #     print("\nYour guess of {guess} is NOT in the hidden word".format(guess = current_guess))
            elif current_guess in guess_list:
                print("\nYou have already guessed {}".format(current_guess))
        elif selection == "2":
            current_guess = input("\nPlease type your full guess to solve: ")
            current_rounds += 1
            if current_guess.lower() == hidden_word.lower():                
                print("\nCongratulations you guessed the word(s)!")
                if current_rounds < shortest_rounds:
                    shortest_rounds = current_rounds
                    print("\nYou have the record for the least amount of guesses.  You solved the word in {} guesses".format(shortest_rounds))
                else:
                    print("\nYou solved the word in {} guesses".format(current_rounds))
                hangman_fnc.continue_playing(username)
                continue_guessing = False
            else:
                print("\nSorry that is incorrect try again.")
                parts_counter += 1
                incorrect_guesses_remaining -= 1
                print("\nYou have {guesses} incorrect guesses remaining ".format(guesses = incorrect_guesses_remaining))
                current_progress = hangman_fnc.show_current_progress(correct_guesses, hidden_word, username)
                print("\n" + current_progress)
        elif selection == "3":
            hangman_fnc.end_game(username)
        else:
            print("Please select a valid option: ")
#hangman_fnc.continue_playing(username)