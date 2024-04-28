import tkinter


def convert_miles_to_km():
    miles = float(entry.get())
    km = miles * 1.6
    ans_label.config(text=round(km, 2))



window = tkinter.Tk()
window.title("mile to km convertor")
window.config(padx=10, pady=10)
entry = tkinter.Entry(width=7)
entry.grid(column=1, row=0)
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)
is_equal_to_label = tkinter.Label(text="Is equal to")
is_equal_to_label.grid(column=0, row=1)
ans_label = tkinter.Label(text="0")
ans_label.grid(column=1, row=1)
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)
calc_button = tkinter.Button(text="Calculate", command=convert_miles_to_km)
calc_button.grid(column=1, row=2)
window.mainloop()
