import tkinter as tk

# Creating the tkinter window 
root = tk.Tk()
#.geometry(x,y):- dimensions
root.geometry("200x500")  
# root window title and dimension
root.title("label")





# creating the label
label = tk.Label(root,
                 text="Label",
                 font=("Arial", 25) )   #assigning the front and text size
label.pack()
#to get text of label
print(label.cget("text"))   
print(label["text"])






# Create a StringVar to associate with the label
text_var = tk.StringVar()
text_var.set("Hello, World!")
label1 = tk.Label(root, 
                  textvariable=text_var)    #if variable change label changes   

label1.pack()
print(text_var.get()) #to get text of label






def inc():
    count = counter["text"]
    counter.configure(text = int(count)+1)      #use configure to change label text

counter = tk.Label(root, 
                   text="1")

counter.pack()

but = tk.Button(root,
              text="increasing",
              command=inc)

but.pack()



root.mainloop()