from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=d60db622fc3edca1d4186e773b422261").json()
    
    # Update weather info labels
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"] - 273.15)) + " °C")
    per_label1.config(text=str(data["main"]["pressure"]) + " hPa")

# Main window
win = Tk()
win.title("Vision College")
win.config(bg="sky blue")
win.geometry("500x570")

# Heading Label
name_label = Label(win, text="Wscube Weather App",
                   font=("Times New Roman", 20, "bold"),
                   bg="sky blue", fg="darkblue")
name_label.place(x=70, y=30, height=50, width=360)

# Dropdown list
list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir",
    "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
    "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Andaman and Nicobar Islands", "Chandigarh",
    "Dadra and Nagar Haveli", "Daman and Diu",
    "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"
]

# City name variable
city_name = StringVar()

# Combobox
com = ttk.Combobox(win, textvariable=city_name, values=list_name, font=("Times New Roman", 15))
com.place(x=25, y=120, height=40, width=450)

# Weather Labels
w_label = Label(win, text="Weather Climate", font=("Times New Roman", 17),
                bg="sky blue", fg="black")
w_label.place(x=25, y=260, height=50, width=210)

w_label1 = Label(win, text="", font=("Times New Roman", 17),
                 bg="sky blue", fg="black")
w_label1.place(x=250, y=260, height=50, width=210)

wb_label = Label(win, text="Weather Description", font=("Times New Roman", 16),
                 bg="sky blue", fg="black")
wb_label.place(x=25, y=330, height=50, width=250)

wb_label1 = Label(win, text="", font=("Times New Roman", 17),
                  bg="sky blue", fg="black")
wb_label1.place(x=250, y=330, height=50, width=250)

temp_label = Label(win, text="Temperature", font=("Times New Roman", 17),
                   bg="sky blue", fg="black")
temp_label.place(x=25, y=400, height=50, width=210)

temp_label1 = Label(win, text="", font=("Times New Roman", 17),
                    bg="sky blue", fg="black")
temp_label1.place(x=250, y=400, height=50, width=210)

per_label = Label(win, text="Pressure", font=("Times New Roman", 17),
                  bg="sky blue", fg="black")
per_label.place(x=25, y=470, height=50, width=210)

per_label1 = Label(win, text="", font=("Times New Roman", 17),
                   bg="sky blue", fg="black")
per_label1.place(x=250, y=470, height=50, width=210)

# Button (calls data_get)
done_button = Button(win, text="Done", font=("Times New Roman", 20, "bold"),
                     command=data_get)
done_button.place(x=200, y=190, height=50, width=100)

win.mainloop()
