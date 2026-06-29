import tkinter as tk
import tkinter.messagebox as messagebox

from quiz import QuizQuestion, Quiz
from validation import validate_name


class QuizApp:

    def __init__(self, root):

        self.root = root
        self.root.title("AI Models Quiz")
        self.quiz = Quiz()

        self.questions = [
            QuizQuestion(
                "1. Finish the sentence: Generative AI...",
                [
                    "A. is used to create models and systems capable of generating new and original content.",
                    "B. acts as a repository for data and content",
                    "C. is a single model that uses code",
                    "D. automates most tasks and can be implemented without research."
                ],
                "A"
            ),
            QuizQuestion(
                "2. Which reasoning process breaks problems into steps?",
                [
                    "A. Diffusion modelling",
                    "B. Predictive modelling",
                    "C. Chain-of-thought",
                    "D. Contextual embedding"
                ],
                "C"
            ),
            QuizQuestion(
                "3. Which is an example of Agentic AI?",
                [
                    "A. Shopping agent that searches across the web",
                    "B. Chatbot used to create fiction stories",
                    "C. Text generator that creates blog posts based on user prompt",
                    "D. AI music creator for YouTube channels"
                ],
                "A"
            ),
            QuizQuestion(
                "4. What is the difference between AI assistants and AI agents?",
                [
                    "A. Same thing",
                    "B. Agents pursue broader goals whilst assistants perform simple, specific tasks.",
                    "C. AI agents require human supervision and AI assistants do not. ",
                    "D. Agents do routine tasks whilst AI assistants are more creative."
                ],
                "B"
            ),
            QuizQuestion(
                "5. Finish the sentence: Agentic AI...",
                [
                    "A. is for creative content only",
                    "B. pursues goals through action cycles and decision making",
                    "C. needs full human direction for every step",
                    "D. only reacts to user prompts."
                ],
                "B"
            )
        ]

        self.current_question = 0

        self.create_start_screen()

    def create_start_screen(self):

        self.name_label = tk.Label(
            self.root,
            text="Enter your name:"
        )
        self.name_label.pack()

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.start_button = tk.Button(
            self.root,
            text="Start Quiz",
            command=self.start_quiz
        )
        self.start_button.pack()

    def start_quiz(self):

        self.name = self.name_entry.get()

        if not validate_name(self.name):
            messagebox.showerror(
                "Error",
                "Please enter your name."
            )
            return

        self.name_label.destroy()
        self.name_entry.destroy()
        self.start_button.destroy()

        self.show_question()

    def show_question(self):

        if self.current_question >= len(self.questions):
            self.show_result()
            return

        question = self.questions[self.current_question]

        self.question_label = tk.Label(
            self.root,
            text=question.question,
            wraplength=400,
            
        )
        self.question_label.pack()

        self.answer_var = tk.StringVar(value="NONE")

        self.radio_buttons = []

        for option in question.options:

            radio = tk.Radiobutton(
                self.root,
                text=option,
                variable=self.answer_var,
                value=option[0],
                bg="lightgreen"
            )

            radio.pack(anchor="w")

            self.radio_buttons.append(radio)

        self.next_button = tk.Button(
            self.root,
            text="Next",
            command=self.next_question
        )

        self.next_button.pack()

    def next_question(self):

        selected = self.answer_var.get()

        if selected == "NONE":
             messagebox.showerror(
            "Answer Required",
            "Please select an answer before continuing."
                            )
             return
        
        question = self.questions[self.current_question]

        self.quiz.check_answer(
            selected,
            question.correct_answer
        )

        self.question_label.destroy()

        for radio in self.radio_buttons:
            radio.destroy()

        self.next_button.destroy()

        self.current_question += 1

        self.show_question()

    


root = tk.Tk()
root.geometry("700x200")
root.configure(background='lightgreen')

app = QuizApp(root)
root.mainloop()