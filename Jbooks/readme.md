# installation

1. create the virtual environment
```bash
python -m venv venv
```
2. activate the virtual environment
```bash
venv\scripts\activate       # for window
source env/bin/activate   # on Mac/Linux
``` 

3. install jupyterlab
```bash
pip install jupyterlab
```

# Beginner Guid

- We use notebooks to write, run, and explain code all in one place — perfect for learning, experimenting, and sharing.

- Jupyter Notebook runs a backend **kernel( engine that runs your code, not your OS kernel )** that executes your code and shows the results right below each cell

- `.ipynb:` The **.ipynb(  Interactive Python Notebook )** extension is used in Jupyter Notebooks because it stores interactive code, output, and text in a JSON format for seamless coding and documentation.

- `cell:` A cell is a block in Jupyter where you can write and run code or text independently.\
**type:** \
**code:** used to write code\
**markdown:** used to write the .md content
- while running the code cell for the first time you need to provide the environment 
- `command/escape mode:` mode in which you can give the command ( press the Esc to enter into the command mode from code mode )
- `code mode:` mode in which you can write the code ( press the enter to enter into the code mode for particular cell )

- **Although it is possible to arrange the cell in unordered format** i.e, use the library in first cell then import them in second cell ( first run the second cell then run the first cell to successful execution )  **always arrange the cells in proper order** eg., load the library in first cell and use that library in second cell( as by default file run from top to bottom ). 

### Keyboard  shortcut (use in command mode)
1. `shift + enter:` execute the enter into the new cell
2. `clt + enter:` execute and stay into the same cell ( press enter to go into the edit mode again )
3. `b:` to create the cell bellow the working cell
4. `a:` to create the cell above the working cell
5. `m:` to convert the current working cell into markdown cell ( press enter to accept the cell change )
6. `y:` to convert the current working cell into code cell ( press enter to accept the cell change )
7. `up/down arrow:` to navigate through the cells ( press the enter to enter into the navigated cell, can also use the j instead of down key and k instead of up key )
8. `dd:` to delete the particular cell 

