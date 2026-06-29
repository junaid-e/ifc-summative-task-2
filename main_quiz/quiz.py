class QuizQuestion:
    """
    question from the quiz:
    """
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer


class Quiz:
    """
    Score is kept:
    """
    def __init__(self):
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        """
        Sees if user answer matches correct answer.
        """

        if user_answer == correct_answer:
            self.score += 1