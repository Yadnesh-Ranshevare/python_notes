import tkinter as tk

# Creating the tkinter window 
root = tk.Tk()
#.geometry(x,y):- dimensions
root.geometry("200x500")  
# root window title and dimension
root.title("Welcome to tkinter")





def but1Click():     #function to call when the user clicks on the button
    print("Button one has clicked!")

def but2Click():     #function to call when the user clicks on the button
    print("Button two has clicked!")


button1 = tk.Button(root,
                   text="button 1",     #text to display on the button
                   command=but1Click)    #command to execute when the user clicks on the button

button2 = tk.Button(root,
                   text="button 2",     #text to display on the button
                   command=but2Click)    #command to execute when the user clicks on the button

# .pack() function adds the child widgets to their parent widget
# padx:- padding along the x axis(in pixels) & pady:- padding along the y axis(in pixels)
button1.pack(padx=20, pady=20)
button2.pack(padx=20, pady=20)





def cancelBut():
    print("canceled!")
    root.destroy()       #destroy the window when cancel button is clicked

cancel = tk.Button(root, 
                   text="cancel", 
                   command=cancelBut)


# Set the position of button to coordinate (100, 20)
cancel.place(x=00, y=150)





def fun1(args):
    print(args)

btn1 = tk.Button(root, 
                text="Press", 
                command=lambda: fun1("by using lambda"))       #lambda function creates a temporary simple function to be called when the Button is clicked.
btn1.pack()


from functools import partial
btn2 = tk.Button(root, text="Click Me", command=partial(
    fun1, "by importing portal"))
btn2.pack()





def openNewWindow():
    newWindow = tk.Toplevel(root)
    newWindow.geometry("200x100")
    newWindow.title("New Window")
    button = tk.Button(newWindow,
              text="close",
              command=newWindow.destroy)
    button.pack()

openNewWindowBtn = tk.Button(root, text="Open New Window", command=openNewWindow)

openNewWindowBtn.pack(pady=20)




from tkinter.ttk import *
# This will create style object
style = Style()
 
# configuring the style object
style.configure('W.TButton', 
                font =('calibri', 10, 'bold', 'underline'),
                foreground = 'red')

btn = Button(root, 
             text = 'Quit !', 
             style = 'W.TButton',    #using that style on button
             command = root.destroy)
# Set the position of button to coordinate (100, 200)
btn.place(x=100, y=200)




# .mainloop() is used to start the event loop
root.mainloop()