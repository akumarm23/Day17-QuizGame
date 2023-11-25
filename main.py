# QUIZ TRIVIA GAME v0.1

# Import the logo, Question class, question data, and QuizBrain class
from art import logo
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Display the game logo
print(logo)

# Create a list of Question objects from the question data
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize the QuizBrain with the question bank
quiz = QuizBrain(question_bank)

# Loop through questions while there are still questions remaining
while quiz.still_has_questions():
    quiz.next_question()

# Display the quiz completion message and the final score
print("\nQUIZ Completed...")
print(f"Final Score:    {quiz.score} / {quiz.question_number}\n")

# END OF CODE
