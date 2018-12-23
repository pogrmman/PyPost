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
        self.frame.grid(row=0, column=0)
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        # Setup requst type selection
        self.req_label = Label(self.frame, text="Request Type:")
        self.req_type = StringVar()
        self.req_type.set("GET")
        self.req_type_get = Radiobutton(self.frame, text="GET", variable=self.req_type, value="GET", indicatoron=False, command=self.set_get)
        self.req_type_post = Radiobutton(self.frame, text="POST", variable=self.req_type, value="POST", indicatoron=False, command=self.set_post)
        self.req_label.grid(row=0, column=0)
        self.req_type_get.grid(row=0, column=1)
        self.req_type_post.grid(row=0, column=2)

        # Setup headers entry
        self.headers = StringVar()
        self.headers_label = Label(self.frame, text="Additional Headers:")
        self.headers_entry = Entry(self.frame, textvariable=self.headers)
        self.headers_label.grid(row=1, column=0)
        self.headers_entry.grid(row=1, column=1, columnspan=2)
        
        # Setup URL entry
        self.url = StringVar()
        self.url_label = Label(self.frame, text="API URL:")
        self.url_entry = Entry(self.frame, textvariable=self.url)
        self.url_label.grid(row=2, column=0)
        self.url_entry.grid(row=2, column=1, columnspan=2)

        # Setup data entry
        self.data = StringVar()
        self.data_label = Label(self.frame, text="Request Data:")
        self.data_entry = Entry(self.frame, textvariable=self.data)
        self.data_label.grid(row=3, column=0)
        self.data_entry.grid(row=3, column=1, columnspan=2)
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
        # Convert data entry to dictionary
        data = self.data.get()
        data_dict = {}
        if data:
            data = data.split("; ")
            for item in data:
                item = item.split("= ")
                data_dict[item[0]] = item[1]
        headers = self.headers.get()
        headers_dict = {}
        # Convert headers entry to dictionary
        if headers:
            headers = headers.split("; ")
            for header in headers:
                header = header.split("= ")
                headers_dict[header[0]] = header[1]
        self.request = pypost.Request(url, request_type=req_type, data=data_dict, headers=headers_dict)
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