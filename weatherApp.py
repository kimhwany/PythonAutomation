import requests
from bs4 import BeautifulSoup
import tkinter as tk

def get_temp():
    # Taking City You Want to Check Temperature
    city_input = city_entry.get()

    # Searching it on google
    search = "weather in" + city_input
    url = f"https://www.google.com/search?&q={search}"

    # Scrape the temperature from the search results
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")

    # Display the temperature
    update = s.find("div", class_="BNeawe").text
    temperature_label.config(text="Temperature in " + city_input + " is: " + update)


# Creating UI widget
root = tk.Tk()
root.geometry('200x200')
city_label = tk.Label(root, text="City: ")
city_entry = tk.Entry(root)

# Button to retrieve temperature
get_temperature_button = tk.Button(root, text="Get Temperature", command=get_temp)
temperature_label = tk.Label(root)

# Positioning the widgets
city_label.pack()
city_entry.pack()
get_temperature_button.pack()
temperature_label.pack()

# Starting main loop
root.mainloop()