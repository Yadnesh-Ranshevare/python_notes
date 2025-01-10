import  tkinter as tk
from tkinter import ttk  # ttk is used for Combobox


# Creating the tkinter window 
root = tk.Tk()
#.geometry(x,y):- dimensions
root.geometry("200x500")  
# root window title and dimension
root.title("menubar")


defaultValue = tk.StringVar() 
defaultValue.set("default")  
comboBox = ttk.Combobox(root,textvariable=defaultValue)

comboBox["value"]=(
    "Python",
    "Java",
    "C++",
    "C#"
)

comboBox.pack()

def submit():
    print("Selected value:", defaultValue.get())

but = tk.Button(root, text="submit", command=submit)
but.pack()





"""fot input with options that appear once you start typing"""
def checkKey(event): 
       
    value = event.widget.get()  # get the value of key that was pressed
    print(value) 
      
    # get data from l 
    if value == '': 
        data = l 
    else: 
        data = [] 
        for item in l: 
            if value.lower() in item.lower(): 
                data.append(item)                 
   
    # update data in listbox 
    update(data)

def update(data): 
      
    # clear previous data 
    lb.delete(0, 'end') 
   
    # put new data 
    for item in data: 
        lb.insert('end', item) 

l = ('C','C++','Java', 
     'Python','Perl', 
     'PHP','ASP','JS' ) 

e = tk.Entry(root) 
e.pack() 
e.bind('<KeyRelease>', checkKey) 

lb = tk.Listbox(root) 
lb.pack()



root.mainloop()