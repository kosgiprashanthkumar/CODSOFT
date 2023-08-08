import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QUIZ GAME")
        self.root.geometry("600x600")
        self.root.configure(bg="white")

        self.question_label = tk.Label(root, text="Question goes here", font=("arial", 16), bg="white")
        self.question_label.pack(pady=20)

        self.radio_var = tk.IntVar()
        self.radio_var.set(-1)

        self.radio_buttons = []
        self.answers = []
        for _ in range(4):
            rb = tk.Radiobutton(root, text="", font=("arial", 15), variable=self.radio_var, value=len(self.answers),
                                fg="blue", bg="white")
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)
            self.answers.append(tk.StringVar())

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.previous_button = tk.Button(self.button_frame, text="Previous", command=self.previous_question, bg="light blue", fg="black")
        self.previous_button.pack(side=tk.LEFT, padx=10)

        self.submit_button = tk.Button(self.button_frame, text="Submit", command=self.check_answer, bg="light green", fg="black")
        self.submit_button.pack(side=tk.LEFT, padx=10)

        self.result_label = tk.Label(root, text="", font=("arial", 14))
        self.result_label.pack()

        self.current_question = 0
        self.correct_answers = 0
        self.user_answers = []

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "Berlin", "Madrid", "Rome"],
                "correct": 0  # Correct answer: Paris
            },
            {
                "question": "Who is the first prime minister of India?",
                "options": ["Indira Gandhi", "Pandit Jawaharlal Nehru", "Lal Bahadur Shastri", "Gulzarilal Nanda"],
                "correct": 1  # Correct answer: Pandit Jawaharlal Nehru
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "correct": 1  # Correct answer: Mars
            },
            {
                "question": "Name the longest river on the Earth?",
                "options": ["Parana River", "Yellow River", "Amazon River", "Nile"],
                "correct": 3  # Correct answer: Nile
            },
            {
                "question": "Name the largest democratic country in the world?",
                "options": ["America", "Russia", "India", "United Kingdom"],
                "correct": 2  # Correct answer: India
            },
            {
                "question": "Name the first man to walk on the Moon?",
                "options": ["Neil Armstrong", "Edwin 'Buzz' Aldrin", "Charles Pete Conrad Jr.", "Alan Bean"],
                "correct": 0  # Correct answer: Neil Armstrong
            },
            {
                "question": "Name the hardest material available on the Earth?",
                "options": ["Gold", "Silver", "Diamond", "Steel"],
                "correct": 2  # Correct answer: Diamond
            },
            {
                "question": "Which is the tallest mountain in the world?",
                "options": ["Kula Kangri", "K2", "Nanga Parbat", "Mount Everest"],
                "correct": 3  # Correct answer: Mount Everest
            },
            {
                "question": "Name the country which is known as the Land of Rising Sun?",
                "options": ["Japan","India","Australia", "China"],
                "correct": 0  # Correct answer: Japan
            },
            {
                "question": "Which is the largest planet in our solar system?",
                "options": ["Earth", "Jupitor", "Mercury", "Saturn"],
                "correct": 1  # Correct answer: Jupitor
            }
            # Add more questions here
        ]

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])

            for idx, option in enumerate(question_data["options"]):
                self.answers[idx].set(option)
                self.radio_buttons[idx].config(textvariable=self.answers[idx])

            self.radio_var.set(-1)
            self.result_label.config(text="")
        else:
            self.question_label.config(text="Quiz completed!")
            self.submit_button.config(state=tk.DISABLED)
            self.previous_button.config(state=tk.DISABLED)
            messagebox.showinfo("Quiz Completed", f"Your score: {self.correct_answers}/{len(self.questions)}")
            self.show_correct_answers()

    def check_answer(self):
        selected_answer = self.radio_var.get()
        correct_answer = self.questions[self.current_question]["correct"]

        self.user_answers.append(selected_answer)

        if selected_answer == correct_answer:
            self.correct_answers += 1
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.result_label.config(text="Wrong!", fg="red")

        # Show correct answer after each question
        correct_option = self.questions[self.current_question]["options"][correct_answer]
        self.result_label.config(text=f"Correct answer: {correct_option}", fg="blue")

        self.current_question += 1
        self.load_question()

    def previous_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.load_question()

    def show_correct_answers(self):
        correct_answers_window = tk.Toplevel(self.root)
        correct_answers_window.title("Correct Answers")

        for idx, question in enumerate(self.questions):
            correct_answer_idx = question["correct"]
            correct_answer = question["options"][correct_answer_idx]
            user_answer_idx = self.user_answers[idx]
            user_answer = question["options"][user_answer_idx] if user_answer_idx != -1 else "Not answered"
            
            answer_label = tk.Label(correct_answers_window, text=f"Q{idx + 1}: {correct_answer}", font=("arial", 12))
            answer_label.pack(anchor="w")

            user_answer_label = tk.Label(correct_answers_window, text=f"Your answer: {user_answer}", font=("arial", 12))
            user_answer_label.pack(anchor="w")

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
