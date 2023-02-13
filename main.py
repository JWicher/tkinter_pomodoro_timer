import math
import tkinter

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
    global reps
    window.after_cancel(timer)
    label_info.config(text="Timer", fg=GREEN)
    canvas.itemconfig(label_time, text="25:00")
    checkmark.config(text="")
    reps = 0

    button_start.config(state="normal")
    button_reset.config(state="disabled")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    reps += 1
    button_start.config(state= "disabled")

    if reps % 8 == 0:
        count_time(LONG_BREAK_MIN * 60)
        label_info.config(text="BREAK", fg=RED)
        button_start.config(state= "normal")
        button_reset.config(state="disabled")

    elif reps % 2 == 0:
        count_time(SHORT_BREAK_MIN * 60)
        label_info.config(text="BREAK", fg=RED)
        button_start.config(state= "normal")
        button_reset.config(state="disabled")

    else:
        count_time(WORK_MIN * 60)
        label_info.config(text="WORK", fg=GREEN)
        button_start.config(state= "disabled")
        button_reset.config(state="normal")

        if reps % 2 == 0:
            checkmark.config(text=f"{'✔'*reps}")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_time(count):
    global timer

    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    formated_time_text = f"{minutes}:{seconds}"
    canvas.itemconfig(label_time, text=formated_time_text)
    if count > 0:
        timer = window.after(1000, count_time, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(padx=100, pady=50, background=YELLOW)
window.title('pomodoro')

# image Pomodoro
image = tkinter.PhotoImage(file="tomato.png")
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=image)
label_time = canvas.create_text(100, 130, text="25:00", fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

# Label Timer
label_info = tkinter.Label(text="Timer", foreground=GREEN, font=(FONT_NAME, 50, 'bold'), highlightthickness=0,
                           bg=YELLOW)
label_info.grid(column=1, row=0)


# button Start
button_start = tkinter.Button(text="start", command=start)
button_start.grid(column=0, row=2)


# button End
button_reset = tkinter.Button(text="reset", command=reset)
button_reset.config(state="disabled")
button_reset.grid(column=2, row=2)


# label Checkmark
checkmark = tkinter.Label(fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 30, 'bold'))
checkmark.grid(column=1, row=3)


window.mainloop()
