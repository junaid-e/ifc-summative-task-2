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
        
   
root = tk.Tk()
root.geometry("700x200")
root.configure(background='lightgreen')

app = QuizApp(root)
root.mainloop()