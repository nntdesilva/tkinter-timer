from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


def start_timer():
    start_button["state"] = DISABLED
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        header.config(text="Break", font=(FONT_NAME, 46), fg=RED, bg=YELLOW)
        counter(long_break_sec)
    elif reps % 2 == 0:
        header.config(text="Break", font=(FONT_NAME, 46), fg=PINK, bg=YELLOW)
        counter(short_break_sec)
    else:
        header.config(text="Work", font=(FONT_NAME, 46), fg=GREEN, bg=YELLOW)
        counter(work_sec)


def counter(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"0{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, counter, count - 1)
    else:
        start_timer()


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# HEADER
header = Label(text="Timer", font=(FONT_NAME, 46), fg=GREEN, bg=YELLOW)
header.grid(column=1, row=0)

# CANVAS
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# START BUTTON
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# RESET BUTTON
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

# CHECK MARK
counters = Label(text="✔", fg=GREEN, bg=YELLOW)
counters.grid(column=1, row=3)

window.mainloop()
