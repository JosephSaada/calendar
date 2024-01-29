from datetime import datetime

class Event:
    def __init__(self, event_id, name, description, date):
        self.event_id = event_id
        self.name = name
        self.description = description
        self.date = date

    def __str__(self):
        return f"Event: {self.name}\nDescription: {self.description}\nDate: {self.date.strftime('%Y-%m-%d')}"

    def get_id(self):
        return self.event_id

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def is_on_date(self, selected_date):
        return self.date.strftime('%Y-%m-%d') == selected_date.strftime('%Y-%m-%d').split(' ')[0]

