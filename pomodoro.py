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

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def time_start():
    global reps
    if reps % 2 == 0:
        count_down(5 * 60)
    elif reps == 8:
        count_down(20 * 60)
    else:
        count_down(1 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro 🍅")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=OFF)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
time_text = canvas.create_text(105, 130, text="00:00", fill="white", font=("gree", 30, "bold"))
canvas.grid(column=1, row=1)

button_one = Button(text="Start", highlightthickness=OFF, command=time_start)
button_one.grid(column=0, row=2)

button_two = Button(text="Reset", highlightthickness=OFF)
button_two.grid(column=2, row=2)


mLabel = Label(fg=GREEN, bg=YELLOW, text="Timer", font=(FONT_NAME, 40, "bold"))
mLabel.grid(column=1, row=0)

mLabel2 = Label(text="✅", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"), highlightthickness=OFF)
mLabel2.grid(column=1, row=3)



window.mainloop()