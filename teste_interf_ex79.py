import tkinter as tk
from tkinter import messagebox

perguntas = [
    {
        "Pergunta": "Quanto é 100²? ",
        "Opções": ["200", "2000", "100", "1000", "10000"],        
        "Resposta": "10000",
    },
    {
        "Pergunta": "Qual a capital da Ucrânia?  ",
        "Opções": ["Lisboa", "Oslo", "Kiev", "Moscou", "Berlim"],        
        "Resposta": "Kiev",
    },
    {
        "Pergunta": "Qual a derivada de x²?  ",
        "Opções": ["x²/2", "x³/3", "x²", "x³", "x"],        
        "Resposta": "x³/3",
    }
]

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz")
        
        self.qtd_acertos = 0
        self.current_question = 0
        
        self.lbl_question = tk.Label(master, text="")
        self.lbl_question.pack()
        
        self.option_buttons = []
        for i in range(5):
            btn = tk.Button(master, text="", command=lambda idx=i: self.check_answer(idx))
            btn.pack(fill=tk.X)
            self.option_buttons.append(btn)
        
        self.next_question()

    def next_question(self):
        if self.current_question < len(perguntas):
            question = perguntas[self.current_question]
            self.lbl_question.config(text=question["Pergunta"])
            options = question["Opções"]
            for i in range(5):
                if i < len(options):
                    self.option_buttons[i].config(text=options[i])
                    self.option_buttons[i].config(state="normal")
                else:
                    self.option_buttons[i].config(text="")
                    self.option_buttons[i].config(state="disabled")
            self.current_question += 1
        else:
            messagebox.showinfo("Fim do Quiz", f"Você acertou {self.qtd_acertos} de {len(perguntas)} perguntas!")

    def check_answer(self, idx):
        question = perguntas[self.current_question - 1]
        if question["Opções"][idx] == question["Resposta"]:
            self.qtd_acertos += 1
            messagebox.showinfo("Resposta", "Acertou!")
        else:
            messagebox.showinfo("Resposta", "Errou!")
        self.next_question()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
