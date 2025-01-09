import  tkinter as tk

# Creating the tkinter window 
root = tk.Tk()
#.geometry(x,y):- dimensions
root.geometry("200x500")  
# root window title and dimension
root.title("label")


def butClick(but):
    print("Button Clicked: ", but)


v = tk.StringVar(root, "1")
# Dictionary to create multiple buttons
values = {"RadioButton 1" : "1",
          "RadioButton 2" : "2",
          "RadioButton 3" : "3",
          "RadioButton 4" : "4",
          "RadioButton 5" : "5"}

for (key, value) in values.items():
    # print(key,value)
    radioButton = tk.Radiobutton(root,
                                 text=key,
                                 variable=v,
                                 value=value,
                                 command=lambda value=value:butClick(value) )      # lambda arguments: expression
    radioButton.pack()


root.mainloop()




