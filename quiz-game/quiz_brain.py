class QuizBrain:
    def __init__(self, questions_list):
        self.questions_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        curr_q = self.questions_list[self.questions_number]
        self.questions_number += 1
        user_ans = input(f"Q.{self.questions_number}: {curr_q.text} (True/False): ")
        self.check_answer(user_ans, curr_q.answer)

    def still_has_questions(self):
        return self.questions_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == "true" or user_answer.lower() == "t":
            user_answer = "true"
        if user_answer == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
            print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.questions_number}\n")
