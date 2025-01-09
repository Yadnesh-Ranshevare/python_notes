import  tkinter as tk

# Creating the tkinter window 
root = tk.Tk()
#.geometry(x,y):- dimensions
root.geometry("200x500")  
# root window title and dimension
root.title("label")




def on_button_toggle():
    if var.get() == 1:
        print("Checkbutton is selected",var.get())
    else:
        print("Checkbutton is deselected",var.get())



# Creating a Checkbutton
var = tk.IntVar()
checkbutton = tk.Checkbutton(root, 
                             text="Enable Feature", 
                             variable=var, 
                             onvalue=1,     #change the value of var to 1 once button is selected
                             offvalue=0,    #change the value of var to 0 once button is disabled
                             command=on_button_toggle)

checkbutton.pack()





text1 = tk.StringVar() 
text2 = tk.StringVar() 
  
#setting the initial value of textVariable to off
text1.set('OFF') 
text2.set('OFF') 
  
chkbtn1 = tk.Checkbutton(root, 
                         textvariable = text1, 
                         variable = text1, 
                         offvalue = 'button not checked',  
                         onvalue = 'button checked') 
chkbtn1.pack(pady=20)


chkbtn2 = tk.Checkbutton(root, 
                         textvariable = text2,
                         variable = text2, 
                         offvalue = 'button not checked', 
                         onvalue = 'button checked')  
chkbtn2.pack(pady=20)






root.mainloop()