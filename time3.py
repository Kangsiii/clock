from tkinter import *
from tkinter import simpledialog
from PIL import ImageTk, Image
import datetime

root = Tk()
root.geometry("665x1440")

image = Image.open("123.png")
image = image.resize((665, 1440), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo)
label.place(x=1280, y=720, anchor=CENTER)

event_date = datetime.datetime.now()

def set_date():
    global event_date
    date_input = simpledialog.askstring("날짜 입력", "날짜를 입력하세요 (YYYY-MM-DD)")
    try:
        event_date = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        date_button.pack_forget()
    except ValueError:
        pass

def time_display():
    current_time = datetime.datetime.now()
    time_left = event_date - current_time
    days_left = time_left.days
    seconds_left = time_left.seconds
    hours_left = seconds_left // 3600
    minutes_left = (seconds_left % 3600) // 60
    seconds_left = (seconds_left % 3600) % 60
    time_string = f"{event_date.strftime('%Y-%m-%d')}까지\n{days_left}일 {hours_left}시간 {minutes_left}분\n열공!!!"
    clock.config(text=time_string)
    clock.after(200, time_display)

clock = Label(root, font=("times", 64, "bold"), bg="#81b9c6")
clock.place(relx=0.5, rely=0.17, anchor=CENTER)

date_button = Button(root, text="날짜 입력", command=set_date)
date_button.pack(pady=20)

time_display()
root.mainloop()