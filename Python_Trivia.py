# -------Created by Yoonhee Park---------
# -------Coding credit: Bro Code---------

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()  # upper letter case
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)
        

# -------part 1--------

def check_answer(answer, guess):
    
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# ---------------

def display_score(correct_guesses, guesses):
    
    print("----------------")
    print("RESULTS")
    print("----------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int(( correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score)+ "%")


# -------part 2--------

def play_again():
    
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

# -------part 3--------

questions = {
    "What is the nearest planet to the sun?: " : "A",
    "How many bones do sharks have?: " : "D",
    "What body part makes us to think?: " : "C",
    "What gas makes up most of the atmosphere of Mars?: " : "B"
}

options = [ ["A. Mercury", "B. Earth", "C. Mars", "D. Venus"],
            ["A. 10", "B. 5", "C. 3", "D. 0"],
            ["A. Eyes", "B. Head", "C. Brain", "D. Ears"],
            ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Argon"] ]

# ---------------

new_game()

while play_again(): 
    new_game()
print("BYEEEE!")