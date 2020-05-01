from tkinter import *
import random
root = Tk()

canvas = Canvas(width=1000, height=800, bg='yellow')
root.resizable(width=False, height=False)

canvas.pack(expand=YES, fill=BOTH)

gif1 = PhotoImage(file='ludo_board.gif')
canvas.create_image(50, 10, image=gif1, anchor=NW)


g3=canvas.create_oval(50, 290, 80, 320, outline="green", fill="green", tags="oval")
g4=canvas.create_oval(50, 390, 80, 420, outline="green", fill="green", tags="oval")

drag_data = {"x":0, "y":0, "item":None}
init_data = {"x":0, "y":0, "item":None}
final_coordinate = [0, 0]



def on_tokken_button_press(event):
    # record the item and its location
    drag_data["item"] = canvas.find_closest(event.x, event.y)[0]
    drag_data["x"] = event.x
    drag_data["y"] = event.y

    init_data["item"] = drag_data["item"]
    init_data["x"] = drag_data["x"]
    init_data["y"] = drag_data["y"]

    item_below = canvas.find_overlapping(event.x, event.y, event.x, event.y)[0]




# when the button is released
def on_tokken_button_release(event):
    # reset the drag information
    drag_data["item"] = None
    drag_data["x"] = 0
    drag_data["y"] = 0
