
from tkinter import *
from PIL import Image, ImageTk

def open_main_game_window():
    main_game_window = Toplevel(root)
    main_game_window.title("Gra w Oczko")
    main_game_window.geometry("1980x1080")
    main_game_window.configure(background = 'black')
    Label(main_game_window, image = background_image).place(relwidth = 1, relheight = 1)

root=Tk()
root.geometry('1980x1080')
root.title('Zacznij Grę w Oczko!')
root.configure(background = "black")

background_image = PhotoImage(file = "background.png")
Label(root, image = background_image).place(relwidth = 1, relheight = 1)

logo = PhotoImage(file = 'logo.png')
button1 = PhotoImage(file = 'button.png')

logo_photo = Label(root, image = logo, background = 'black')
logo_photo.pack(fill=BOTH)


starting_button = Button(root, image = button1, command = open_main_game_window, background = 'black')
starting_button.pack(expand=TRUE)

root.mainloop()
