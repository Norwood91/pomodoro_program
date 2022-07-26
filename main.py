# ---------------------------- CONSTANTS ------------------------------- #
import tkinter



PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#ecb390"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title('The Pomodoro Technique')
window.config(padx=100, pady=50, bg=PINK)

canvas = tkinter.Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.pack()












window.mainloop()
