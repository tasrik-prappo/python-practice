questions: tuple = ("How many elements are in the periodic table?: ",
                    "Which animal lays the largest eggs?: ",
                    "What is the most abundant gas in Earth's atmosphere?: ",
                    "How many bones are in the human body?: ",
                    "Which planet in the solar system is the hottest?: "
                    )

options: tuple = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers: tuple = ("C", "D", "A", "A", "B")

score: int = 0
question_num: int = 0

for question in questions:

    print("--------------------------------------------------")
    print(question)
    print(options[question_num])

    guess: str = input("Enter A,B,C,D,E: ").upper()

    if guess == answers[question_num]:
        print("Correct!")
        score += 1

    else:
        print("Incorrect!")
        print(f"Correct answer is {answers[question_num]}")

    question_num += 1


print(f"Your final score is: {score}/5")


