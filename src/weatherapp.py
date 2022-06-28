import tkinter as tk
import requests
from tkinter import font

HEIGHT = 500
WIDTH = 600


# 840c0cc0f1db7fea9fd459d3926089ce my key
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
def test_function(entry):
    print('The entry is: ', entry)


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'location: ' + str(name) + '\n' + str(desc) + '\n' + str(temp) + 'F'
    except:
        final_str = 'error getting data'
    return final_str

def get_weather(city):
    weather_key = '840c0cc0f1db7fea9fd459d3926089ce'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='jamjam.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#50c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Maiandra GD', 19))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Show Weather', font=('Maiandra GD', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Maiandra GD', 19), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)
# print(tk.font.families())


root.mainloop()
