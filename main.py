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
r_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    reps = 0
    window.after_cancel(r_timer)
    title.config(text='Timer', background=YELLOW, font=(FONT_NAME, 30, 'bold'), fg=GREEN)
    time_text.itemconfig(timer_text, text='00:00')
    check_marks.config(text='')



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        title.config(text='Break', fg=PINK)
    elif reps % 2 == 0:
        countdown(break_sec)
        title.config(text='Break', fg=RED)
    else:
        countdown(work_sec)
        title.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(time_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global r_timer
        r_timer = window.after(1000, countdown, count - 1)
    else:
        start()
        marks = ''
        work_session = math.floor(reps/2)
        for n in range(work_session):
            marks += '✔'
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=60, pady=20, bg=YELLOW)


title = Label(text='Timer', background=YELLOW, font=(FONT_NAME, 30, 'bold'), fg=GREEN)
title.grid(column=1, row=0)

start_button = Button(text='Start', command=start)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset)
reset_button.grid(column=2, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 110, image=tomato_img)

time_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 33, 'bold'))
canvas.grid(column=1, row=1)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()