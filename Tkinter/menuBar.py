import  tkinter as tk


# Creating the tkinter window 
root = tk.Tk()
#.geometry(x,y):- dimensions
root.geometry("200x500")  
# root window title and dimension
root.title("menubar") 



menubar = tk.Menu(root)

root.config(menu=menubar)



file = tk.Menu(menubar, tearoff = 0)    #to create menubar option 
menubar.add_cascade(label ='File', menu = file)     #to add it into the frame
# adding option  in the menubar
file.add_command(label ='New File', command = None) 
file.add_command(label ='Open...', command = None) 
file.add_command(label ='Save', command = None)
file.add_separator()    #insert the line between the options
file.add_command(label ='Exit', command = root.destroy) 

edit = tk.Menu(menubar, tearoff =0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='cut', command =None)
edit.add_command(label ='copy', command = None)
edit.add_command(label ='paste', command = None)
edit.add_separator() #insert the line between the options
edit.add_command(label ='exit', command = root.destroy)


#similar to html dropdown
helpList = ["help", "tk help","about us"]       #option to showcase in dropdown
option = tk.StringVar(root)
option.set("help us")   #option to show by default
helpMenu = tk.OptionMenu(root,option,*helpList)
helpMenu.pack()

def printOPtion():
    print("You selected:", option.get())

submit_button = tk.Button(root, text='Submit', command=printOPtion) 
submit_button.pack()


L = tk.Label(
    root, 
    text ="Right-click to display menu", 
    width = 40, 
    height = 20,
    background ="red", 
    relief ="sunken", 
    cursor ="hand2",  #change the cursor to hand when hovering over the label
) 
L.pack()
m = tk.Menu(root, tearoff = 0) 
m.add_command(label ="Cut") 
m.add_command(label ="Copy") 
m.add_command(label ="Paste") 
m.add_command(label ="Reload") 
m.add_separator() 
m.add_command(label ="Rename") 

def do_popup(event): 
    try: 
        m.tk_popup(event.x_root, event.y_root) 
    finally: 
        m.grab_release() 
  
L.bind("<Button-3>", do_popup) 



root.mainloop()