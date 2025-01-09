import  tkinter as tk

# Creating the tkinter window 
root = tk.Tk()
#.geometry(x,y):- dimensions
root.geometry("200x500")  
# root window title and dimension
root.title("label")


def go(event):
    # print("Double Clicked on item number", event.widget.curselection()[0] + 1)
    # selected_item()    # calling the function to print selected item's text
    
    
    css =  listBox.curselection()        #.curselection() is a method of the Listbox widget that returns a tuple of indices representing the currently selected items
    label["text"] = listBox.get(css)
    print(css)
    # Setting Background Colour 
    for list in css: 
          
        if list == 0: 
            root.configure(background='red') 
        elif list == 1: 
            root.configure(background='green') 
        elif list == 2: 
            root.configure(background='yellow') 
        elif list == 3: 
            root.configure(background='white') 


listBox = tk.Listbox(root,
                     selectmode="single",)
listBox.insert(1,"red")
listBox.insert(2,"green")
listBox.insert(3,"yellow")
listBox.insert(4,"white")

listBox.bind('<Double-1>', go)

listBox.pack()

# Creating Edit box to show selected option 
label = tk.Label(root, 
                 text='Default') 
label.pack() 


def selected_item():
    for i in listBox.curselection():    #.curselection() is a method of the Listbox widget that returns a tuple of indices representing the currently selected items
        print(listBox.get(i))
 

btn = tk.Button(root, 
                text='Print Selected', 
                command=selected_item)

btn.pack(side='bottom')

root.mainloop()  # Start the GUI event loop. This will keep the window open until we close it.
