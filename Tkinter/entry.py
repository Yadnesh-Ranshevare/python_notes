import tkinter as tk

# Creating the tkinter window 
root = tk.Tk()
#.geometry(x,y):- dimensions
root.geometry("200x500")  
# root window title and dimension
root.title("label")





# declaring string variable
# for storing entry data
name_var=tk.StringVar()
pass_var=tk.StringVar()

def submit():
    print("Name:",name_var.get())
    print("Password:",pass_var.get())
    name_var.set("")
    pass_var.set("")
    entry.focus()   # focus on entry widget when submission is successful

username = tk.Label(root,
                    text= "Username",)
username.pack()

entry = tk.Entry(root,
                 textvariable=name_var)     #assigning the string variable as entry text
entry.pack()

password = tk.Label(root,
                    text= "Password")
password.pack()

entry_pass = tk.Entry(root,
                     textvariable=pass_var,
                     show="*")
entry_pass.focus_force()    #focus_force is used to take focus as soon as application starts 
entry_pass.pack()

submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.pack()







my_entry = tk.StringVar()
my_entry.set("disabled entry")

entry_disabled = tk.Entry(root, 
                          textvariable=my_entry, 
                          state="disabled")

entry_disabled.pack(pady=20)

root.mainloop()