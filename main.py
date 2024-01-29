import tkinter as tk
from tkinter import messagebox
import user

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title('Login System')
        self.user_list = {'': '', 'user2': 'password2'}

        # Username Label and Entry
        self.label_username = tk.Label(root, text='Username:')
        self.label_username.pack(pady=10)
        self.entry_username = tk.Entry(root)
        self.entry_username.pack(pady=10)

        # Password Label and Entry
        self.label_password = tk.Label(root, text='Password:')
        self.label_password.pack(pady=10)
        self.entry_password = tk.Entry(root, show='*')
        self.entry_password.pack(pady=10)

        # Login Button
        self.btn_login = tk.Button(root, text='Login', command=self.login)
        self.btn_login.pack(pady=10)

        # Create Account Button
        self.btn_createUser = tk.Button(root, text='Create Account', command=self.createUser)
        self.btn_createUser.pack(pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in self.user_list and self.user_list[username] == password:
            self.root.withdraw()
            user.UserWindow(username)
        else:
            messagebox.showerror('Login Failed', 'Incorrect username or password')

    def createUser(self):
        new_username = self.entry_username.get()
        new_password = self.entry_password.get()

        if new_username and new_password:
            self.user_list[new_username] = new_password
            messagebox.showinfo('Account Created', 'Account for {} created successfully'.format(new_username))
        else:
            messagebox.showerror('Invalid Input', 'Please enter a valid username and password')

def main():
    root = tk.Tk()
    main_instance = Main(root)
    root.mainloop()

if __name__ == '__main__':
    main()
