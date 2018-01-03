#! /usr/bin/python

"""
This is a simple txt editor
"""

__author__ = "Archiebald Meat Pants"
__copyright__ = "Copyright 2017, eddie Project"
__credits__ = ["Some Name", "Another Name", "New Name", "A Name"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Rick Sanchez"
__email__ = "User@example.com"
__status__ = "Development"

from Tkinter import *
from tkFileDialog import *
from tkSimpleDialog import askstring


class EgUi:
    """
    This is the eddie window class
    """

    def __init__(self, master):
        self.master = master
        master.title("eddie")
        master.minsize(width=600, height=350)
        master.iconbitmap('./images/winicon.ico')

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # Set "file_name" to a default (Untitled.txt)
        self.file_name = "Untitled.txt"

        # create the file menu objects
        file_menu = Menu(menu, tearoff=False)
        edit_menu = Menu(menu, tearoff=False)
        tools_menu = Menu(menu, tearoff=False)
        help_menu = Menu(menu, tearoff=False)

        # Add sub menu items to the "File" menu and define commands to execute on selection:
        file_menu.add_command(label="New", command=self.create_new_file)
        file_menu.add_command(label="Open", command=self.open_existing_file)
        file_menu.add_separator()
        file_menu.add_command(label="Save", command=self.save_open_file)
        file_menu.add_command(label="Save As", command=self.save_open_file_as)
        file_menu.add_command(label="Close", command=self.close_open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Print", command=self.print_open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.destroy)

        # Add sub menu items to the "Edit" menu and define commands to execute on selection:
        edit_menu.add_command(label="Cut", command=self.do_nothing)
        edit_menu.add_command(label="Copy", command=self.do_nothing)
        edit_menu.add_command(label="Paste", command=self.do_nothing)
        edit_menu.add_separator()
        edit_menu.add_command(label="Delete", command=self.do_nothing)
        edit_menu.add_command(label="Undo", command=self.do_nothing)
        edit_menu.add_separator()
        edit_menu.add_command(label="Find", command=self.do_nothing)
        edit_menu.add_command(label="Find Next", command=self.do_nothing)
        edit_menu.add_command(label="Replace", command=self.do_nothing)
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=self.do_nothing)

        # Add sub menu items to the "Tools" menu and define commands to execute on selection:
        tools_menu.add_command(label="Settings", command=self.do_nothing)

        # Add sub menu items to the "Help" menu and define commands to execute on selection:
        help_menu.add_command(label="Documentation", command=self.do_nothing)
        help_menu.add_separator()
        help_menu.add_command(label="About eddie", command=self.do_nothing)

        # Display the sub menu items
        menu.add_cascade(label="File", menu=file_menu)
        menu.add_cascade(label="Edit", menu=edit_menu)
        menu.add_cascade(label="Tools", menu=tools_menu)
        menu.add_cascade(label="Help", menu=help_menu)

        # Create a tool bar
        self.tool_bar = Frame(self.master, bg="grey", height=30)
        # Create toolbar objects here

        # Display the tool bar
        # self.tool_bar.pack(side="top", fill=X)
        self.tool_bar.grid(row=0, column=0, columnspan=1)

        # Create the entry text area
        self.text_box = Text(self.master, highlightthickness=0, bd=1)

        # Create a status bar
        self.status_bar = Label(self.master, text="No open document ...", bd=1, relief=SUNKEN, anchor=W)
        # self.status_bar.pack(side=BOTTOM, fill=X)
        self.status_bar.grid(row=3,column=0)

    # ******************************************************************************************************************
    # *************************************** Class method Declarations: ***********************************************
    # ******************************************************************************************************************

    @staticmethod
    def do_nothing():
        print("I do nothing I did nothing")
        return

    @staticmethod
    def get_file_name():
        # Get a file name from the user
        fn = askstring('File name', 'Enter a file name:')
        fn = fn + ".txt"
        return fn

    # **************************
    # File Menu Methods:
    # **************************

    def create_new_file(self):

        # Delete anything that might already be in the text box
        self.text_box.delete(0.0, END)

        # Display the text box
        self.text_box.pack(expand=True, fill='both')

        # Set the status bar text
        self.status_bar.config(text="Untitled.txt")

        return

    def open_existing_file(self):
        # Ask the user to select a file
        f = askopenfile(mode='r')

        # Test to see if askopenfile returned a file path, if not return
        if not f:
            return

        # If a file path was returned open it
        else:
            t = f.read()
            self.file_name = f.name.strip('.')
            self.text_box.delete(0.0, END)
            self.text_box.insert(0.0, t)
            self.text_box.pack(expand=True, fill='both')
            self.status_bar.configure(text=self.file_name)
        return

    def save_open_file(self):
        if self.file_name == "Untitled.txt":
            self.file_name = self.get_file_name()
        t = self.text_box.get(0.0, END)
        f = open(self.file_name, 'w')
        f.write(t)
        f.close()
        self.status_bar.config(text=self.file_name)
        return

    def save_open_file_as(self):
        f = asksaveasfile(mode='w', defaultextension='.txt')
        self.file_name = f.name.strip('.')
        t = self.text_box.get(0.0, END)
        f.write(t.rstrip())
        self.status_bar.config(text=self.file_name)
        return

    def close_open_file(self):
        self.file_name = None
        self.text_box.delete(0.0, END)
        self.text_box.pack_forget()
        self.status_bar.configure(text="Ready")
        return

    @staticmethod
    def print_open_file():
        message_text = """

            Not implemented.

                   """
        message_window = Tk()
        message_window.title("eddie Message ...")
        message_window.iconbitmap('.\images\winicon.ico')
        message_window.minsize(width=300, height=75)
        message_window.maxsize(width=300, height=75)
        message_notification = Label(message_window, text=message_text, height=0, width=0, borderwidth=1, anchor="w")
        message_notification.pack(side="left")
        message_window.mainloop()
        return

    def cut_selection(self):
        # Method to close the currently opened file
        return

    def copy_selection(self):
        # Method to close the currently opened file
        return

    def paste_selection(self):
        # Method to close the currently opened file
        return

    def delete_selection(self):
        # Method to close the currently opened file
        return

    def undo_action(self):
        # Method to close the currently opened file
        return

    def find_text(self):
        # Method to close the currently opened file
        return

    def find_next_instance(self):
        # Method to close the currently opened file
        return

    def replace_pattern(self):
        # Method to close the currently opened file
        return

    def select_all(self):
        # Method to close the currently opened file
        return

    def xed_settings(self):
        # Method to close the currently opened file
        return

    def eddie_documents(self):
        # Method to close the currently opened file
        return

    def eddie_about(self):
        # Method to close the currently opened file
        return


# Create the root window
root = Tk()

# Create a window class instance and associate it with the root window
eddie_gui = EgUi(root)

# Start the main loop process
root.mainloop()
