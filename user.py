import sys
import tkinter as tk
import settings
import objCalendar
import tkinter.simpledialog
import tkinter.ttk as ttk

class UserWindow:
    def __init__(self, name):
        self.user_window = tk.Toplevel()
        self.user_window.title('User Window - {}'.format(name))

        self.btn_create_calendar = tk.Button(self.user_window, text='Create Calendar', command=self.create_calendar)
        self.btn_open_calendar = tk.Button(self.user_window, text='Open Calendar', command=self.open_calendar)
        self.btn_delete_calendar = tk.Button(self.user_window, text='Delete Calendar', command=self.delete_calendar)
        self.btn_view_public_calendar = tk.Button(self.user_window, text='View Public Calendar', command=self.view_public_calendar)
        self.btn_open_settings = tk.Button(self.user_window, text='Open Settings', command=self.open_settings)
        self.btn_logout = tk.Button(self.user_window, text='Logout', command=self.logout)

        self.btn_create_calendar.pack(pady=10)
        self.btn_open_calendar.pack(pady=10)
        self.btn_delete_calendar.pack(pady=10)
        self.btn_view_public_calendar.pack(pady=10)
        self.btn_open_settings.pack(pady=10)
        self.btn_logout.pack(pady=10)

        self.calendars = []

    def create_calendar(self):
        calendar_name = tkinter.simpledialog.askstring("Calendar Name",
                                                       "Enter the name of your calendar")
        if calendar_name:
            new_calendar = objCalendar.objCalendar(calendar_name)
            self.calendars.append(new_calendar)

    def open_calendar(self):
        if not self.calendars:
            print("No calendars available.")
            return

        select_calendar_window = tk.Toplevel()
        select_calendar_window.title('Select Calendar')

        listbox = tk.Listbox(select_calendar_window, selectmode = tk.SINGLE)

        for i, calendar in enumerate(self.calendars, start = 1):
            listbox.insert(tk.END, f"{i}. {calendar.get_name()}")

        def open_selected_calendar():
            selected_index = listbox.curselection()
            if selected_index:
                selected_calendar_index = int(selected_index[0])
                selected_calendar = self.calendars[selected_calendar_index]
                objCalendar.objCalendar.open(selected_calendar)
                select_calendar_window.destroy()
            else:
                print("Please select a calendar.")

        open_button = tk.Button(select_calendar_window, text = "Open Calendar",
                                command = open_selected_calendar)
        open_button.pack(pady = 10)

        listbox.pack(padx = 10, pady = 10)


    def delete_calendar(self):
        if not self.calendars:
            print("No calendars available.")
            return

        select_calendar_window = tk.Toplevel()
        select_calendar_window.title('Select Calendar to Delete')

        listbox = tk.Listbox(select_calendar_window, selectmode = tk.SINGLE)

        for i, calendar in enumerate(self.calendars, start = 1):
            listbox.insert(tk.END, f"{i}. {calendar.get_name()}")

        def delete_selected_calendar():
            selected_index = listbox.curselection()
            if selected_index:
                selected_calendar_index = int(selected_index[0])
                selected_calendar = self.calendars[selected_calendar_index]
                self.calendars.remove(selected_calendar)
                select_calendar_window.destroy()
            else:
                print("Please select a calendar.")

        delete_button = tk.Button(select_calendar_window, text = "Delete Calendar",
                                    command = delete_selected_calendar)
        delete_button.pack(pady = 10)

        listbox.pack(padx = 10, pady = 10)

    def view_public_calendar(self):
        print("not in use")

    def open_settings(self):
        settings.Settings(tk.Toplevel())

    def logout(self):
        self.user_window.destroy()
        print("Logging out")
        sys.exit()
