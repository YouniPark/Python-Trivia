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

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")


# -------part 2--------

def play_again():
    return 0


# -------part 3--------

questions = {
    "question: ": "Answer"}

options = [["A. sth", "B. sth", "C. sth", "D. sth"]]

# ---------------

new_game()

while play_again():
    new_game()
print("BYEEEE!")