from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    Timer.config(text='Timer')
    check.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        Timer.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        Timer.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        Timer.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            mark += '✔'
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('TOMATO')
window.config(padx=40, pady=40, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(102, 130, text='00:00', font=('Libre Baskerville', 30, 'bold'), fill='white')
canvas.grid(column=1, row=1)

Timer = Label(text='Timer', font=('arial', 30), bg=YELLOW, fg=GREEN)
Timer.config(pady=10)
Timer.grid(column=1, row=0)

start = Button(text='Start', font=('Libre Baskerville', 15), highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text='Reset', font=('Libre Baskerville', 15), highlightthickness=0, command=reset)
reset.grid(column=2, row=2)

check = Label(font=('arial', 30), bg=YELLOW, fg=GREEN)
check.config(pady=10)
check.grid(column=1, row=3)

window.mainloop()
