# ---------------------------- CONSTANTS ------------------------------- #
import tkinter
import math

WHITE = '#ffffff'
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#65c18c"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        main_label['text'] = 'Break'
    elif reps % 2 == 0:
       countdown(short_break_sec)
       main_label['text'] = 'Break'
    else:
       countdown(work_sec)
       main_label['text'] = 'Study!'


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✔'
        checkmark_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title('The Pomodoro Technique')
window.config(padx=100, pady=50, bg=PINK)


main_label = tkinter.Label(text='Timer', fg=WHITE, font=(FONT_NAME, 35, 'bold'), bg=PINK)
main_label.grid(column=1, row=0)


canvas = tkinter.Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

checkmark_label = tkinter.Label(fg= WHITE, bg=PINK, font=(FONT_NAME, 20, 'bold'))
checkmark_label.grid(column=1, row=3)

reset_button = tkinter.Button(text='Reset')
reset_button.grid(column=2, row=2)


window.mainloop()
