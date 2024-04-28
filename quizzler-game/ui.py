from tkinter import *
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, brain):
        self.q_brain = brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(self.window, text="Score: 0", fg="white", bg=THEME_COLOR, pady=10)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(self.window)
        self.canvas.config(height=250, width=300, bg="white", highlightthickness=0)
        self.q_text = self.canvas.create_text(150, 125, width=280, text="", font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.v_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(self.window, image=self.v_img, highlightthickness=0, command=lambda: self.check_answer("true"))
        self.true_btn.grid(row=2, column=0)
        self.x_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(self.window, image=self.x_img, highlightthickness=0, command=lambda: self.check_answer("false"))
        self.false_btn.grid(row=2, column=1)
        self.get_next_q()
        self.window.mainloop()

    def get_next_q(self):
        self.canvas.config(bg="white")
        if self.q_brain.still_has_questions():
            next_q = self.q_brain.next_question()
            self.canvas.itemconfig(self.q_text, text=next_q)
        else:
            self.canvas.itemconfig(self.q_text, text="No more questions")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def check_answer(self, user_ans):
        right, score = self.q_brain.check_answer(user_ans)
        self.score_label.config(text=f"Score: {score}")
        if right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_q)


