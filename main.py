import tkinter as tk
from functools import partial

WIDTH, HEIGHT = 1000, 700
TEXT_BOX = "#F1F8E8"
FONT = ("Arial", 22)
is_writing = False
timer_id = None
sec = 0


def countdown(count):
    global timer_id
    if count >= 0 and not is_writing:
        print(timer_id, "running")
        timer_id = window.after(1000, countdown, count - 1)
    elif is_writing:
        print(timer_id, "stop")
        window.after_cancel(timer_id)
        countdown(5)


def keyup(event):
    global is_writing, sec
    # print("key up")
    is_writing = False
    sec += 1
    print(sec)



def keydown(event):
    global is_writing, sec
    # print("key down")
    is_writing = True
    sec = 0
    print(sec)


def notwriting():
    text_box.delete('1.0', tk.END)
    print("not wrinting")


window = tk.Tk()

window.title("Disappearing Text")
window.minsize(WIDTH, HEIGHT)
window.config(pady=10)

text_box = tk.Text(window,
                   background=TEXT_BOX,
                   borderwidth=4,
                   font=FONT,
                   height=20,
                   width=60,
                   padx=2,
                   pady=2
                   )
text_box.pack(expand=True)
text_box.focus_set()

text_box.bind('<KeyRelease>', keyup)
text_box.bind('<KeyPress>', keydown)
# countdown(5)

window.mainloop()
