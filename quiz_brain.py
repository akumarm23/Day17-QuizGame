class QuizBrain():
    def __init__(self, q_list):
        # Initialize QuizBrain with a list of questions, question number, and score.
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    
    def still_has_questions(self):
        # Check if there are still questions remaining in the question list.
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Get the next question from the question list, ask the user, and check the answer.
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {current_question.text} (True / False):  ").lower()
        self.check_answer(user_answer, current_question.answer)
    
    def check_answer(self, user_answer, correct_answer):
        # Check if the user's answer matches the correct answer, update score, and provide feedback.
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("\nYou are Correct!\n")
        else:
            print("\nSorry, Wrong answer.\n")
        # Display the correct answer and the current score.
        print(f"The correct answer is:  {correct_answer}")
        print(f"Current Score:  {self.score} / {self.question_number}\n")
