### Builtins ###
import pprint
## Tkinter ##
from tkinter import Tk, ttk
from tkinter import Label, Radiobutton, Button, Entry, Text
from tkinter import StringVar
from tkinter import N, S, E, W
from tkinter import INSERT, END
### Project Imports ###
import pypost

### GUI Specification ###
class PyPostGUI:
    def __init__(self, master):
        # Set master and title
        self.master = master
        master.title("PyPost REST API Tester " + pypost.VERSION)

        # Setup layout
        self.frame = ttk.Frame(master, padding=(10,10,10,10))
        self.frame.grid(row=0, column=0, sticky=N+S+E+W)
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=0)
        self.frame.rowconfigure(0, weight=0)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=0)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(2, weight=0)
        self.frame.rowconfigure(3, weight=0)
        self.frame.rowconfigure(4, weight=0)
        self.frame.rowconfigure(5, weight=1)

        # Setup requst type selection
        self.req_label = Label(self.frame, text="Request Type:")
        self.req_type = StringVar()
        self.req_type.set("GET")
        self.req_type_get = Radiobutton(self.frame, text="GET", variable=self.req_type, value="GET", indicatoron=False, command=self.set_get)
        self.req_type_post = Radiobutton(self.frame, text="POST", variable=self.req_type, value="POST", indicatoron=False, command=self.set_post)
        self.req_label.grid(row=0, column=0)
        self.req_type_get.grid(row=0, column=1, sticky=E+W)
        self.req_type_post.grid(row=0, column=2, sticky=E+W)

        # Setup headers entry
        self.headers = StringVar()
        self.headers_label = Label(self.frame, text="Additional Headers:")
        self.headers_entry = Entry(self.frame, textvariable=self.headers)
        self.headers_label.grid(row=1, column=0)
        self.headers_entry.grid(row=1, column=1, columnspan=2, sticky=E+W)
        
        # Setup URL entry
        self.url = StringVar()
        self.url_label = Label(self.frame, text="API URL:")
        self.url_entry = Entry(self.frame, textvariable=self.url)
        self.url_label.grid(row=2, column=0)
        self.url_entry.grid(row=2, column=1, columnspan=2, sticky=E+W)

        # Setup data entry
        self.data = StringVar()
        self.data_label = Label(self.frame, text="Request Data:")
        self.data_entry = Entry(self.frame, textvariable=self.data)
        self.data_label.grid(row=3, column=0)
        self.data_entry.grid(row=3, column=1, columnspan=2, sticky=E+W)
        self.data_label.grid_remove()
        self.data_entry.grid_remove()

        # Request button
        self.request_button = Button(self.frame, text="Make Request", command=self.make_request)
        self.request_button.grid(row=4, column=0, columnspan=3, sticky=N+S+E+W)

        # Response
        self.response = Text(self.frame)
        self.response.grid(row=5, column=0, columnspan=3, sticky=N+S+E+W)
        self.response.grid_remove()

    def set_get(self):
        self.data_label.grid_remove()
        self.data_entry.grid_remove()

    def set_post(self):
        self.data_label.grid()
        self.data_entry.grid()

    def make_request(self):
        url = self.url.get()
        req_type = self.req_type.get()
        headers = self.headers.get()
        if headers:
            headers = pypost.process_data(headers)
        data = None
        if req_type == "POST":
            data = self.data.get()
            data = pypost.process_data(data)
        self.request = pypost.Request(url, request_type=req_type, data=data, headers=headers)
        self.request.fetch()
        # Reformat dictionary as string
        response = pprint.pformat(self.request.response)
        # Update response text
        self.response.config(state="normal")
        self.response.delete(1.0, END)
        self.response.insert(INSERT, response)
        self.response.config(state="disabled")
        self.response.grid()
        
### Run GUI ###
root = Tk()
gui = PyPostGUI(root)
root.mainloop()
