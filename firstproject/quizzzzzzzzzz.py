qsns = [
    {"qsn": "What is the Sum of 2 + 2?", "answer": "4"},
    {"qsn": "What is the Sum of 3 + 2?", "answer": "5"},
    {"qsn": "What is the Sum of 4 + 2?", "answer": "6"},
    {"qsn": "What is the Sum of 5 + 2?", "answer": "7"},
]

def quiz():
    score = 0
    print("Welcome to the quiz!")
    for question in qsns:
        print(question["qsn"])  # Print the current question
        user_answer = input("Your answer: ")  # Get the user's answer
        
        # Check if the user's answer matches the correct answer
        if user_answer == question["answer"]:
            print("Correct Answer")
            score += 1  # Increment the score for a correct answer
        else:
            print("Incorrect answer. The correct answer is:", question["answer"])  # Show the correct answer

    # Show the final score
    print("\nYou scored", score, "out of", len(qsns))

# Check if the script is being run directly
if __name__ == "__main__":
    quiz()  # Run the quiz function
