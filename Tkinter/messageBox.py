import  tkinter as tk
from tkinter import messagebox

# Creating the tkinter window 
root = tk.Tk()
#.geometry(x,y):- dimensions
root.geometry("200x500")  
# root window title and dimension
root.title("message box") 



w = tk.Label(root, text ='GeeksForGeeks', font = "50")  
w.pack() 
  
messagebox.showinfo("message", "Information") 
  
messagebox.showwarning("showwarning", "Warning") 
  
messagebox.showerror("showerror", "Error") 
  
que = messagebox.askquestion("askquestion", "Are you sure?") 
print(que)  #yes or no
  
isOk = messagebox.askokcancel("askokcancel", "Want to continue?") 
print(isOk)  #True or False
  
isFind = messagebox.askyesno("askyesno", "Find the value?") 
print(isFind)   #True or False

  
res = messagebox.askretrycancel("askretrycancel", "Try again?")
print(res)    #True or False

  
root.mainloop()  