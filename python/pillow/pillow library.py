from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title('My Photo Album')
window.geometry('400x420')

title = Label(window, text = 'My photo Album', fg = 'white', bg = 'purple', width = 40)
title.pack(pady = 10)
img_file = Image.open('python/pillow/app_img.jpg')
img_file = img_file.resize((300,180))
photo = ImageTk.PhotoImage(img_file)
pic = Label(window, image = photo)
pic.pack(pady = 5)

def show_message():
    messagebox.showinfo('Great!','You have opened the picture.')
msg_btn = Button(window, text = 'Click to react', fg = 'white', bg = 'blue', command = show_message)
msg_btn.pack(pady = 5)

def show_details():
    top = Toplevel()
    top.title('photo details')
    top.geometry('200x120')
    info = Label(top, text = 'Taken on: 1 June 2025.')
    info.pack(pady = 10)
    place = Label(top, text = 'My Garden.')
    place.pack()
    top.mainloop()
details_btn = Button(window , text = 'See Details', bg = 'green', fg  = 'white', command = show_details)
details_btn.pack(pady = 10)

window.mainloop()