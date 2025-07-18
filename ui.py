from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=450, height=600, bg=THEME_COLOR, padx=20, pady=20)
        self.board = Canvas(width=250, height=300, background="white")
        self.question_text = self.board.create_text(125, 150,
                                                    width=250,
                                                    fill=THEME_COLOR,
                                                    text=f"Question Prompt",
                                                    font=("Arial", 20, "italic"))
        self.board.grid(row=1,column=0, columnspan=2, pady=50)
        self.score_board = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_board.grid(row=0, column=1)
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.check_btn = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.check_btn.grid(row=2, column=0)
        self.cross_btn = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.cross_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.board.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_board.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.board.itemconfig(self.question_text, text=q_text)
        else:
            self.board.itemconfig(self.question_text, text=f"You reached the end of the quiz\n"
                                                           f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.check_btn.config(state="disabled")
            self.cross_btn.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.board.config(bg="green")
        else:
            self.board.config(bg="red")
        self.window.after(1000, self.get_next_question)
