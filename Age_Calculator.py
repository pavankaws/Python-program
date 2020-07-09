from tkinter import *

from tkcalendar import DateEntry

window = Tk()

window.title("Age Calculator")

window.geometry('350x200')

lbldob = Label(window, text="Date of Birth")

lbldob.grid(column=0, row=0)

txtdob = DateEntry(window, width=10)

txtdob.grid(column=1, row=0)

lbltodate = Label(window, text="To Date")

lbltodate.grid(column=0, row=1)

txttodate = DateEntry(window, width=10)

txttodate.grid(column=1, row=1)

btn = Button(window, text="Calculate", command=calval)

btn.grid(column=2, row=0)

def calval():
    dob = txtdob.get_date()
    print(dob)
    todate = txttodate.get_date()
    print(todate)
    # get years in DOB
    dobyears = dob.years
    todateyears = todate.years
    resnoofyears = int(todateyears) - int(dobyears)

    # get months in DOB
    dobmonths = dob.months
    todatemonths = todate.months
    resnoofmonths = resnoofyears * 12 + dobmonths - todatemonths

    # get days in DOB
    dobdays = dob.days
    resdays = resnoofyears * 365 + resnoofmonths * 30 + dobdays

    print("Years:" + resnoofyears)
    print("months:" + resnoofmonths)
    print("Days:" + resdays)




window.mainloop()
