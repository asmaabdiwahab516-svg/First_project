
import random

# STEP 1: Create a list of questions
questions = [
    {
        "question": "2. Which symbol is used to assign a value to a variable?",
        "choices": ["A. =", "B. ==", "C. +", "D. /"],
        "answer": "A"
    },
    {
        "question": "Which language are we learning?",
        "choices": ["A. Java", "B. Python", "C. C++", "D. HTML"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "choices": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "Which function displays something on the screen?",
        "choices": ["A. input()", "B. print()", "C. type()", "D. len()"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a function?",
        "choices": ["A. for", "B. if", "C. while", "D. def"],
        "answer": "D"
    }
]

# STEP 2: Mix the questions randomly
random.shuffle(questions)

# STEP 3: Create a score variable
score = 0

# STEP 4: Welcome the player

print("WELCOME TO THE QUIZ!")

# STEP 5: Loop through every question
for question in questions:

    print("\n" + question["question"])

    # Display the four choices
    for choice in question["choices"]:
        print(choice)

    # STEP 6: Collect the user's answer
    while True:
        try:
            user_answer = input("Enter your answer (A/B/C/D): ").upper()

            if user_answer not in ["A", "B", "C", "D"]:
                raise ValueError("Please enter A, B, C, or D.")

            break

        except ValueError as error:
            print(error)

    # STEP 7: Check whether the answer is correct
    if user_answer == question["answer"]:
        print("Correct! Well done!")
        score += 1

    else:
        print("Wrong answer!")
        print("The correct answer is:", question["answer"])

# STEP 8: Calculate the final percentage
total_questions = len(questions)
percentage = (score / total_questions) * 100

# STEP 9: Display the final results
print("\n" "QUIZ RESULTS")

print("Your score:", score, "/", total_questions)
print("Your percentage:", percentage, "%")

# STEP 10: Give feedback
if percentage >= 80:
    print("Excellent! You are amazing!")

elif percentage >= 50:
    print("Good! Keep practicing!")

else:
    print("Try Again! You can do better!")

print("THANK YOU FOR PLAYING!")

