import tkinter as tk

WIDTH, HEIGHT = 1000, 700
TEXT_BOX = "#F1F8E8"
FONT = ("Arial", 22)
is_writing = False
timer_ids = []
sec = True


def countdown(count):
    global is_writing, sec
    if is_writing:
        for ids in timer_ids:
            window.after_cancel(ids)
        timer_ids.clear()
        sec = True
        is_writing = False
        keyup('<KeyRelease>')

    elif count >= 0 and not is_writing:
        timer_id = window.after(1000, countdown, count - 1)
        timer_ids.append(timer_id)
    else:
        sec = True
        text_box.delete('1.0', tk.END)


def keyup(event):
    global is_writing, sec
    if sec:
        window.after_idle(countdown, 5)
        sec = False
        is_writing = False


def keydown(event):
    global is_writing
    if not sec:
        is_writing = True


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

window.mainloop()
