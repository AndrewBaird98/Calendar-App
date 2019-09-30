import tkinter as tk
from tkinter import font  as tkfont

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("Event Planner")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=5)
        container.grid_columnconfigure(0, weight=5)

        self.frames = {}
        for F in (StartPage, EventPage, AccountPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=10, column=10, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10, padx = 10)

        button1 = tk.Button(self, text="Go to Page One", command=lambda: controller.show_frame("EventPage"))
        button2 = tk.Button(self, text="Go to Page Two", command=lambda: controller.show_frame("AccountPage"))
        button1.pack()
        button2.pack()
        textentry = tk.Text(self, width=20, height=1, wrap=tk.WORD, background="white")
        textentry.pack(side =tk.TOP)


class EventPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="EventPage", font=controller.title_font)
        label.pack(side="top", fill="x", pady=100, padx = 100)
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        button.pack()


class AccountPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AccountPage", font=controller.title_font)
        label.pack(side="top", fill="x", pady=100, padx = 100)
        button = tk.Button(self, text="Go to the start page",  command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()