from tkinter import *
from tkinter import filedialog, simpledialog, ttk
import pikepdf
from tkcalendar import Calendar, DateEntry


# function to get the file and remove password for the file
def getfile():
    # getting file from the user to remove the password
    filename = filedialog.askopenfilename(title="select file",
                                          filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    # Getting the password fromt he user to open the file
    USER_INP = simpledialog.askstring(title="Test",
                                      prompt="Enter the password:")
    # Open the pdf file using pidepdf method and with the given password
    removepassw = pikepdf.open(filename, USER_INP)
    # Saving the password removed file
    removepassw.save(filename + "unlocked.pdf")
    lblunlock = Label(root, text="Unlocked and saved in same path")
    lblunlock.place(relx=0.5, rely=0.7, anchor=CENTER)



root = Tk()
root.title("Password Removal Utility")
# set window size
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{width}x{height}')
# Notebook needs to be created to craete frames(each farme will be treated like a tab)
# creating Notebook to have tabs in the screen
my_notebook = ttk.Notebook(root)
my_notebook.pack()
# Defining tabs
my_frame1 = Frame(my_notebook, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
my_frame2 = Frame(my_notebook, width=root.winfo_screenwidth(), height=root.winfo_screenheight())

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)
# Adding frames to the notebook
my_notebook.add(my_frame1, text="Password Removal Utility")
my_notebook.add(my_frame2, text="Interest Calculator")
# to have the controls in each tab need to give Frame name(my_frame1)


# Controls for my_frame1(Password Removal Utility)
lbl = Label(my_frame1, text="Select the file to remove the password")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
btn = Button(my_frame1, text="Choose file", command=getfile)
btn.place(relx=0.62, rely=0.5, anchor=CENTER)
# Controls for my_frame1(Password Removal Utility)



root.mainloop()
