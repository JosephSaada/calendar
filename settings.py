import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz

class Settings:
    def __init__(self, root):
        self.root = root
        self.root.title('Settings')
        self.root.geometry('300x300')
        self.root.configure(bg='white')

        self.label_timezone = tk.Label(self.root, text='Timezone:')
        self.label_timezone.pack()

        timezones = ["GMT", "America/New_York", "America/Los_Angeles", "Europe/Berlin"]

        self.timezone_var = tk.StringVar()
        self.timezone_combobox = ttk.Combobox(self.root, textvariable=self.timezone_var, values=timezones)
        self.timezone_combobox.pack()

        self.label_time = tk.Label(self.root, text='Time:')
        self.label_time.pack()

        self.label_time_value = tk.Label(self.root, text=self.get_current_time())
        self.label_time_value.pack()

        self.label_date = tk.Label(self.root, text='Date:')
        self.label_date.pack()

        self.label_date_value = tk.Label(self.root, text=datetime.now().strftime('%d/%m/%Y'))
        self.label_date_value.pack()

        self.btn_change_timezone = tk.Button(self.root, text='Change Timezone', command=self.changeTimezone)
        self.btn_change_timezone.pack()

        self.btn_close = tk.Button(self.root, text='Close', command=self.root.destroy)
        self.btn_close.pack()

        self.root.mainloop()

    def changeTimezone(self):
        new_timezone = self.timezone_var.get()
        if new_timezone:
            self.label_timezone.configure(text='Timezone: {}'.format(new_timezone))
            self.label_time_value.configure(text=self.get_current_time(new_timezone))
            self.label_date_value.configure(text=datetime.now().strftime('%d/%m/%Y'))
        else:
            self.label_timezone.configure(text='Timezone: {}'.format(''))
            self.label_time_value.configure(text=self.get_current_time())
            self.label_date_value.configure(text=datetime.now().strftime('%d/%m/%Y'))

    def get_current_time(self, timezone="America/Los_Angeles"):
        utc_time = datetime.utcnow()
        utc_timezone = pytz.timezone('UTC')
        selected_timezone = pytz.timezone(timezone)

        utc_time = utc_timezone.localize(utc_time)
        converted_time = utc_time.astimezone(selected_timezone)
        return converted_time.strftime('%H:%M:%S')

