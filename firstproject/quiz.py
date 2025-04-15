# Simple Quiz Game

# List of questions with options and the correct answer
quiz_data = [
    {
        "q": "What is the capital of France?",  # Question text
        "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],  # List of answer options
        "answer": "A"  # Correct answer (key)
    },
    {
        "q": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "q": "Who wrote 'Hamlet'?",
        "options": ["A) Mark Twain", "B) Charles Dickens", "C) William Shakespeare", "D) Jane Austen"],
        "answer": "C"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "answer": "C"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Great White Shark"],
        "answer": "B"
    }
]

# Function to conduct the quiz
def run_quiz():
    score = 0  # Initialize the score to 0

    print("Welcome to the Quiz Game!")  # Welcome message
    print("Please answer the following questions:\n")  # Instructions for the user

    # Loop through each question in the quiz_data
    for question in quiz_data:
        print(question["question"])  # Print the question text
        for option in question["options"]:
            print(option)  # Print each option for the current question

        # Get the user's answer, strip whitespace, and convert to uppercase
        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!\n")  # Inform the user if their answer is correct
            score += 1  # Increment the score
        else:
            # Inform the user if their answer is wrong and show the correct answer
            print(f"Wrong! The correct answer was {question['answer']}.\n")

    # Show the final score to the user
    print(f"Your final score is {score}/{len(quiz_data)}.")  # Show the number of correct answers out of total questions
    print("Thank you for playing!")  # End message

# Entry point of the program
if __name__ == "__main__":
    run_quiz()  # Call the function to run the quiz
