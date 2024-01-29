from datetime import datetime
from tkinter import *
from tkcalendar import Calendar, DateEntry
import event
import random

class objCalendar:
    def __init__(self, name):
        self.name = name
        self.eventSet = []

    def get_name(self):
        return self.name

    def updateEvent(self):
        update_event_window = Toplevel()
        update_event_window.title("Update Event")

        event_listbox = Listbox(update_event_window, selectmode = SINGLE, height = 10, width = 40)
        event_listbox.pack(pady = 10)

        for event in self.eventSet:
            event_listbox.insert(END, event.get_name())

        def on_event_select(event):
            selected_index = event_listbox.curselection()
            if selected_index:
                selected_event = self.eventSet[selected_index[0]]
                update_event_popup(selected_event)

        event_listbox.bind("<ButtonRelease-1>", on_event_select)

        def update_event_popup(selected_event):
            update_popup = Toplevel()
            update_popup.title("Update Event")

            lbl_name = Label(update_popup, text = "Event Name:")
            lbl_name.pack()
            entry_name = Entry(update_popup)
            entry_name.insert(END, selected_event.get_name())  # Set default value
            entry_name.pack()

            lbl_description = Label(update_popup, text = "Event Description:")
            lbl_description.pack()
            entry_description = Entry(update_popup)
            entry_description.insert(END, selected_event.get_description())  # Set default value
            entry_description.pack()

            lbl_date = Label(update_popup, text = "Event Date:")
            lbl_date.pack()
            entry_date = DateEntry(update_popup, width = 12, background = 'darkblue',
                                   foreground = 'white', borderwidth = 2)
            entry_date.set_date(selected_event.date)  # Set default value
            entry_date.pack()

            def update_event():
                name = entry_name.get()
                description = entry_description.get()
                date = entry_date.get_date()

                if name and description and date:
                    selected_event.set_name(name)
                    selected_event.set_description(description)
                    selected_event.date = date
                    print("Event updated successfully.")
                    update_popup.destroy()
                else:
                    print("Invalid input. Please fill in all fields.")

            btn_update = Button(update_popup, text = "Update Event", command = update_event)
            btn_update.pack()

        def close():
            update_event_window.destroy()

        btn_close = Button(update_event_window, text = "Close", command = close)
        btn_close.pack(pady = 10)

        update_event_window.mainloop()

    def deleteEvent(self):
        delete_event_window = Toplevel()
        delete_event_window.title("Delete Event")

        event_listbox = Listbox(delete_event_window, selectmode = SINGLE, height = 10,
                                width = 40)
        event_listbox.pack(pady = 10)

        for event in self.eventSet:
            event_listbox.insert(END, event.get_name())

        def on_event_select(event):
            selected_index = event_listbox.curselection()
            if selected_index:
                selected_event = self.eventSet[selected_index[0]]
                confirm_delete_popup(selected_event)

        event_listbox.bind("<ButtonRelease-1>", on_event_select)

        def confirm_delete_popup(selected_event):
            confirm_delete_popup = Toplevel()
            confirm_delete_popup.title("Confirm Deletion")

            confirmation_label = Label(confirm_delete_popup,
                                       text = f"Are you sure you want to delete {selected_event.get_name()}?")
            confirmation_label.pack(pady = 10)

            def delete_event():
                self.eventSet.remove(selected_event)
                print("Event deleted successfully.")
                delete_event_window.destroy()
                confirm_delete_popup.destroy()

            btn_confirm_delete = Button(confirm_delete_popup, text = "Yes, Delete",
                                        command = delete_event)
            btn_confirm_delete.pack(pady = 10)

            btn_cancel_delete = Button(confirm_delete_popup, text = "Cancel",
                                       command = confirm_delete_popup.destroy)
            btn_cancel_delete.pack()

        def close():
            delete_event_window.destroy()

        btn_close = Button(delete_event_window, text = "Close", command = close)
        btn_close.pack(pady = 10)

        delete_event_window.mainloop()

    def setPublic(self):
        print("Not in use")

    def shareCalendar(self):
        print("Not in use")

    def createEvent(self):
        create_event_window = Toplevel()
        create_event_window.title("Create Event")

        lbl_name = Label(create_event_window, text="Event Name:")
        lbl_name.pack()
        entry_name = Entry(create_event_window)
        entry_name.pack()

        lbl_description = Label(create_event_window, text="Event Description:")
        lbl_description.pack()
        entry_description = Entry(create_event_window)
        entry_description.pack()

        lbl_date = Label(create_event_window, text="Event Date:")
        lbl_date.pack()
        entry_date = DateEntry(create_event_window, width=12, background='darkblue', foreground='white', borderwidth=2)
        entry_date.pack()

        def create_event():
            name = entry_name.get()
            description = entry_description.get()
            date = entry_date.get_date()

            if name and description and date:
                event_id = random.randint(1000, 9999)
                new_event = event.Event(event_id, name, description, date)
                self.eventSet.append(new_event)
                print("Event created successfully.")
                create_event_window.destroy()
            else:
                print("Invalid input. Please fill in all fields.")

        btn_create = Button(create_event_window, text="Create Event", command=create_event)
        btn_create.pack()

    def visualize(self):
        visualize_window = Toplevel()

        visualize_window.geometry("400x400")

        today = datetime.today()
        cal = Calendar(visualize_window, selectmode = 'day',
                       year = today.year,
                       month = today.month,
                       day = today.day)

        cal.pack(pady = 20)

        event_text = Text(visualize_window, height = 10, width = 40)
        event_text.pack(pady = 10)

        def update_event_text(selected_date):
            event_text.delete(1.0, END)
            events_on_date = [event for event in self.eventSet if event.is_on_date(selected_date)]
            for event in events_on_date:
                event_text.insert(END, f"{event}\n")

        def on_date_select(event):
            selected_date_str = cal.get_date()
            selected_date = datetime.strptime(selected_date_str, "%m/%d/%y")
            update_event_text(selected_date)

        cal.bind("<<CalendarSelected>>", on_date_select)
        on_date_select(today)

        def close():
            visualize_window.destroy()

        btn_close = Button(visualize_window, text = "Close", command = close)
        btn_close.pack(pady = 10)

        visualize_window.mainloop()

    def open(self):
        calendar = Toplevel()
        calendar.title(self.name)

        btn_create_event = Button(calendar, text='Create Event', command=self.createEvent)
        btn_update_event = Button(calendar, text='Update Event', command=self.updateEvent)
        btn_delete_event = Button(calendar, text='Delete Event', command=self.deleteEvent)
        btn_set_public = Button(calendar, text='Set Public', command=self.setPublic)
        btn_share_calendar = Button(calendar, text='Share Calendar', command=self.shareCalendar)
        btn_visualize = Button(calendar, text='Visualize', command=self.visualize)

        btn_create_event.pack(pady=10)
        btn_update_event.pack(pady=10)
        btn_delete_event.pack(pady=10)
        btn_set_public.pack(pady=10)
        btn_share_calendar.pack(pady=10)
        btn_visualize.pack(pady=10)
