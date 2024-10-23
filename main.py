# import tkinter
# from tkinter import Button, Entry
#
# #Create window
# window = tkinter.Tk()
# window.title("My GUI")
# window.minsize(width=500,height=300)
# window.config(padx = 20, pady = 20 )
#
# #Label
# my_label = tkinter.Label(text="I am a label", font = ("Arial", 24, "bold"))
# my_label.grid(column = 0, row = 0)
#
# # #Button
# # def clicked():
# #     text = "clicked"
# #     my_label.config(text = text)
# #     my_label.pack()
# # button = Button(text="Click me", command=clicked)
# # button.pack()
#
# def clicked():
#     input_text = input.get()
#     my_label.config(text=input_text)
#     my_label.pack()
# button = Button(text="Click me", command = clicked)
# button.grid(column = 1, row = 1)
#
# button2 = Button(text="Button 2", command = clicked)
# button2.grid(column = 2, row = 0)
#
#
# #Entry (Input)
# input = Entry(width=10)
# input.grid(column = 4, row = 3)
#
#
# window.mainloop()

# Hackathon in tkinter
# Mile -> KM converter

import tkinter

#Create window
window = tkinter.Tk()
window.title("Miles -> Km converter")

#Entry
input = tkinter.Entry()
input.grid(column = 1, row = 0)
input.config(width=10)

# Create label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column = 2, row = 0)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column = 0, row = 1)

km_label = tkinter.Label(text="Km")
km_label.grid(column = 2, row = 1)

convert_number_label = tkinter.Label(text="0")
convert_number_label.grid(column = 1, row = 1)

#def converter func

def calculate():
    miles = input.get()
    km = round(float(miles) * 1.60934, 3)
    convert_number_label.config(text = km)

#Create button
calculate_button = tkinter.Button(text="Calculate", command = calculate)
calculate_button.grid(column = 1, row = 2)



window.mainloop()
